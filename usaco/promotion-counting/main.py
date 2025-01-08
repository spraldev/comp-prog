bronze = []
silver = []
gold = []
platinum = []

with open("promote.in", "r") as f:
    bronze = list(map(int, f.readline().strip().split()))
    silver = list(map(int, f.readline().strip().split()))
    gold = list(map(int, f.readline().strip().split()))
    platinum = list(map(int, f.readline().strip().split()))

platinum_promotions = platinum[1] - platinum[0]
gold_promotions = platinum_promotions + gold[1] - gold[0]
silver_promotions = gold_promotions + silver[1] - silver[0]

with open("promote.out", "w") as f:
    f.write(str(silver_promotions) + "\n")
    f.write(str(gold_promotions) + "\n")
    f.write(str(platinum_promotions) + "\n")