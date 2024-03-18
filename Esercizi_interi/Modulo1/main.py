import random
codici = list(range(1,27))
random.shuffle(codici)
lettere  = []
for n in range(65,91):
    lettere.append(chr(n))
    diz ={}
for idx, c in enumerate(lettere):
    diz[c] = codici[idx]
print(diz)