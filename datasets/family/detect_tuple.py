
def main(args):
    fact_list = []
    with open('./facts.txt') as f:
        lines = f.readlines()
        for line in lines:
            facts = line.strip().split('\t')
            if facts[1] == args.r:
                fact_list.append(facts)

    for fact_1 in fact_list:
        a_1, _, b_1 = fact_1
        for fact_2 in fact_list:
            a_2, _, b_2 = fact_2
            if a_2 == b_1:
                print(fact_1, '\t', fact_2)

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r")
    args = parser.parse_args()
    main(args)


