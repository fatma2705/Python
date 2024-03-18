'''
scrivere una procedura che prende in input una lista di interi e da come output 
l'indice del massimo
'''

def TrovaMassimoList(lListaInteri):
    # Dobbiamo scorrere una ad uno i numeri della lista e 
    # salvarci da una parte il massimo
    tipo1 = type(lListaInteri)
    IndiceMassimo = 0
    IndiceCorrente = 0 
    for i in lListaInteri:
        if i > lListaInteri[IndiceMassimo]:
            IndiceMassimo = IndiceCorrente
        IndiceCorrente += 1
    return IndiceMassimo

def TrovaMinimo(lListaInteri):
    IndiceMinimo = 0
    IndiceCorrente = 0 
    for a in lListaInteri:
        if a < lListaInteri[IndiceMinimo]:
            IndiceMinimo = IndiceCorrente
        IndiceCorrente += 1
    return IndiceMinimo

def TrovaMassimoDict(myDict):
    iPrimoElemento = 1
    IndiceMassimo = 0 
    sChiaveMax =  ""
    for k,v in myDict.items():
        if iPrimoElemento == 1:
            IndiceMassimo = v
            iPrimoElemento = 0
        if v > IndiceMassimo:
            sChiaveMax = k
            IndiceMassimo = v
    return sChiaveMax

def TrovaMassimo(dati):
    tipo = type(dati)
    if tipo == list:
        TrovaMassimoList(dati)
    elif tipo == dict:
        TrovaMassimoDict(dati)
    else:
        print("Attenzione tipo dati errato ")
        return "Error"




print("Programma principale")
lListaVotiMario = [12,34,56,7,89,90, 55, 36]
lListaESamiMario = ["fisica", "chimica", "meccanica1", "meccanica2", "geometria", "analisi1", "analisi2", "chimica organica"]
IrisPrecedura = -1
IrisPrecedura = TrovaMassimoList(lListaVotiMario)
print(f" L'esame in cui Mario ha preso il voto massimo è {lListaESamiMario[IrisPrecedura]}")
IrisPrecedura = -1
IrisPrecedura = TrovaMinimo(lListaVotiMario)
#print(f" L'esame in cui Mario ha preso il voto minimo è {lListaESamiMario[IrisPrecedura]}")

DizionarioEsamiMario = {"fisica":12 , "chimica":56,"maccanica1":33, "meccanica2":44 ,
"geometria":99 , " analisi1":77,"analisi2":52, "chimica organica":70}
IrisPrecedura = TrovaMassimoDict(DizionarioEsamiMario)

print(f" L'esame in cui Mario ha ottenuto il voto massimo è {IrisPrecedura}")
print(f" e il voto è {DizionarioEsamiMario[IrisPrecedura]}")




    