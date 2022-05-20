import argparse

def parse_amie_rules(facts):
    with open(facts, "r", encoding="utf-8") as f:
        with open(facts+".inv", 'w', encoding="utf-8") as g:
            lines = f.readlines()
            for line in lines:
                t, r, h = line.strip().split('\t')
                inv_r =  "inv_" + r
                w = line + "{}\t{}\t{}\n".format(h, inv_r, t)
                g.write(w)
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--facts")
    args = parser.parse_args()
    parse_amie_rules(args.facts)

