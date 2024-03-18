'''
data una stringa , una lista di parole stampare a schermo la prima parole della lista che c'è nella  
'''
lista = ["Mario","gino","antonio"]
stringa = ("Oggi gino e Mario si deveno incontrare")
iminimo = len(stringa)
sminimo = lista[0]
for elemento in lista :
    pos = stringa.find(elemento)
    if pos >= 0 and pos < iminimo:
        iminimo = pos
        sminimo = elemento
print(f" il minimo è {sminimo} nella posizione {iminimo}")