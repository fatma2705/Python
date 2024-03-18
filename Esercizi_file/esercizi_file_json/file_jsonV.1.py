import json

listaStudenti = []
dictStudenti =  {}
pathFile = "/home/studente113/dati.json"

while True:
    nome = input("inserisci nome :  (oppure scrivi 'stop' per terminare) ")
    if nome.lower() == "stop":
        break
    cognome = input("inserisci cognome :  ")
    facoltà = input("inserisci facoltà :  ")
    dictStudenti["nome"] = nome
    dictStudenti["cognome"] = cognome
    dictStudenti["facoltà"] = facoltà
    listaStudenti.append(dictStudenti)
    print(listaStudenti)
    
with open(pathFile, "w") as f:
    json.dump(listaStudenti, f)