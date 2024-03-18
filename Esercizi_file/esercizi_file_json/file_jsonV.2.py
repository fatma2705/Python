import json

opr = input("Operazione 1)per scrivere un file json con i dati dei studenti , 2) per aggiungere uno o più studenti a un file già esistente :  ") 
if opr == "1":
        listaStudenti = []

        dictStudenti =  {}
        pathFile = "/home/studente113/dati.json"
        while True:
            nome = input("inserisci nome :  (oppure scrivi 'stop' per terminare) ")
            if nome.lower() == "stop":
                break
            cognome = input("inserisci cognome :  ")
            facoltà = input("inserisci facoltà :  ")
            dictStudenti = {"nome": nome, "cognome": cognome, "facoltà": facoltà}
            listaStudenti.append(dictStudenti)
            print(listaStudenti)
            with open(pathFile, "w") as f:
                json.dump(listaStudenti, f)
        
if opr == "2":
        lista = []
        nomeFile = input("inserisci nome file :")
        nStudenti = int(input("inserisci numeri studenti che vuoi aggiungere :"))
        PathFile = "/home/studente113/" + nomeFile + ".json"
        f = open(PathFile,"r")
        contenuto = f.read()
        f.close()
        lista = json.loads(contenuto)
        for i in range (0,nStudenti):
            nome = input("inserisci nome : ")
            cognome = input("inserisci cognome :  ")
            facoltà = input("inserisci facoltà :  ")
            dictStudenti2 = {"nome": nome, "cognome": cognome, "facoltà": facoltà}
            lista.append(dictStudenti2)
        with open(PathFile, "w") as f:
            json.dump(lista, f)
