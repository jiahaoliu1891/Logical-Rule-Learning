from data import *
import copy
import re
import torch
import numpy as np
from collections import defaultdict
import argparse
from utils import *


def remove_var(r):
    """R1(A, B), R2(B, C) --> R1, R2"""
    r = re.sub(r"\(\D?, \D?\)", "", r)
    return r


def parse_rule(r):
    """parse a rule into body and head"""
    r = remove_var(r)
    head, body = r.split(" <-- ")
    body = body.split(", ")
    return head, body


def load_rules(rule_path):
    rule_list = []
    with open(rule_path, 'r') as f:
       rules = f.readlines()
       for rule in rules:
            conf, r = rule.strip('\n').split('\t')
            conf_1, conf_2 = float(conf[0:5]), float(conf[-6:-1])
            head, body = parse_rule(r)
            # rule item: (head, body, conf_1, conf_2)
            rule_list.append((head, body, conf_1, conf_2))
    return rule_list


def get_connected(list1, list2):
    conn = []   
    for e1 in list1:
        h1, t1 = e1[0], e1[-1]
        for e2 in list2:
            h2, t2 = e2[0], e2[-1]
            if t1 == h2:
                path = e1[0:-1] + e2
                conn.append(path)
    return conn


def predict(head, body, ground_rdf):
    pred = []
    length = len(body)
    body_entity = []
    for b_ in body:
        entities = [] 
        for rdf in ground_rdf:
            fact = parse_rdf(rdf)
            h, r, t = fact
            if r == b_:
                entities.append([h,t])
        body_entity.append((b_, entities))
    
    if length == 1:
        b,entities = body_entity[0]
        for e in entities:
            h,t = e
            pred.append((h, head, t))
    else:
        for i_ in range(length-1):
            if i_ == 0:
                _, t1_list = body_entity[i_]
                _, t2_list = body_entity[i_+1]
                connections = get_connected(t1_list, t2_list) 
            else:
                _, t2_list = body_entity[i_+1]
                connections = get_connected(connections, t2_list)
        for conn in connections:
            h, t = conn[0], conn[-1]
            pred.append((h, head, t))        
    return pred


def rdf2set(rdfs):
    sets = set()
    for rdf in rdfs:
        tuples = parse_rdf(rdf)
        sets.add(tuples)    
    return sets


def coverage(rules, dataset, output):
    """
    Input a set of rules
    """
    # rdf_data
    fact_rdf, train_rdf, valid_rdf, test_rdf = dataset.fact_rdf, dataset.train_rdf, dataset.valid_rdf, dataset.test_rdf
    # relation
    rdict = dataset.get_relation_dict()
    head_rdict = dataset.get_head_relation_dict()
    rel2idx, idx2rel = rdict.rel2idx, rdict.idx2rel
    # entity
    idx2ent, ent2idx = dataset.idx2ent, dataset.ent2idx
    e_num = len(idx2ent)
    predictions = []
    """rdf to set"""
    test_set = rdf2set(test_rdf)
    train_set = rdf2set(train_rdf)
    valid_set = rdf2set(valid_rdf) 
    fact_set = rdf2set(fact_rdf)
    all_set = fact_set | train_set | valid_set
    """Prediction"""
    pred_set = set()
    for r in rules:
        head, body, _, _ = r
        pred_list = predict(head, body, fact_rdf+train_rdf)
        for pred in pred_list:
            if pred not in all_set:
                pred_set.add(pred) 
    pred_num = len(pred_set)
    test_num = len(test_set)
    overlap = len(pred_set&test_set)
    coverage = overlap / test_num
    print("pred number:{}, test number:{}, overlap:{}".format(pred_num, test_num, overlap))
    print("Coverage: {}".format(coverage))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rule", default='amie_top48.txt', help="increase output verbosity")
    parser.add_argument("--data_idx", type=int, default=1, help="increase output verbosity")
    args = parser.parse_args()
    print_msg("Coverage Test")
    print("Rule: {}".format(args.rule))

    # Load data from *.txt
    dataset_name = ["fb15k-237", "family"]
    data_path = '../datasets/{}/'.format(dataset_name[args.data_idx])
    dataset = Dataset(data_root=data_path, inv=True)
    print("Dataset: {}".format(data_path))

    rules = load_rules(args.rule)
    coverage(rules, dataset, output='amie_top48_results.txt')

