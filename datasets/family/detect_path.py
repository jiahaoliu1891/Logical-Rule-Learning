def main(args):
    fact_r1_list = []
    fact_r2_list = []
    all_facts = []
    head2feq = {}
    N_all, N_loop = 0, 0
    with open('./facts.txt.inv') as f:
        lines = f.readlines()
        for line in lines:
            facts = line.strip().split('\t')
            all_facts.append(facts)
            if facts[1] == args.r1:
                fact_r1_list.append(facts)
            if facts[1] == args.r2:
                fact_r2_list.append(facts)

    for fact_1 in fact_r1_list:
        a_1, r_1, b_1 = fact_1
        for fact_2 in fact_r2_list:
            a_2, r_2, b_2 = fact_2
            if a_1 == b_2 and r_2 == args.r2:
                N_all += 1
                for f_ in all_facts:
                    if f_[0] == a_2 and f_[2] == b_1:
                        N_loop += 1
                        print('------------------------------')
                        print("{} -[{}]-> {} -[{}]-> {}".format(b_1, r_1, a_1, r_2, a_2))
                        print("{} -[{}]-> {}".format(f_[2], f_[1], f_[0]))
                        if f_[1] not in head2feq:
                            head2feq[f_[1]] = 1
                        else:
                            head2feq[f_[1]] += 1
    print(N_loop, '/', N_all)
    print(head2feq)

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r1")
    parser.add_argument("-r2")
    args = parser.parse_args()
    print(args.r1, args.r2)
    main(args)


