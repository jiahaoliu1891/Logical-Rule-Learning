from collections import defaultdict

rel2fact = defaultdict(list)

fact_list = []
with open('./facts.txt') as f:
    lines = f.readlines()
    for line in lines:
        facts = line.strip().split('\t')
        rel2fact[facts[1]].append((facts[0], facts[2]))


for k, v in rel2fact.items():
    print(k, len(v))



