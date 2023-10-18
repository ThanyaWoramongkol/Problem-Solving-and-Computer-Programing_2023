"""CatParade"""

def cats():
    """-"""
    parnd = []
    now = ""
    while True:
        gene = input()
        if gene == "END":
            break
        if "," in gene:
            speci = gene.split(", ")
            parnd += speci
        elif gene == "IT'S A DOG":
            del parnd[-1]
        else:
            parnd.append(gene)
    store = sorted(parnd)
    for i in store:
        seem = "%s %d %d" % (i, parnd.index(i) + 1, parnd.count(i))
        if seem == now:
            continue
        now = seem
        print(seem)
    print(store)
cats()
     