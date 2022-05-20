def main():
    e_list = []
    with open('./facts.txt') as f:
        lines = f.readlines()
        for line in lines:
            facts = line.strip().split('\t')
            if facts[0] not in e_list:
                e_list.append(facts[0])
            if facts[2] not in e_list:
                e_list.append(facts[2])
            
    with open('./facts.txt') as f:
        lines = f.readlines()
        for line in lines:
            facts = line.strip().split('\t')
            if facts[0] in e_list[0:10] and facts[2] in e_list[0:10]:
                print(facts)

if __name__ == '__main__':
    main()


