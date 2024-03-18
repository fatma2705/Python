'''
scrivi un programma in cui l'utente inserisce una stringa che è un'operazione :es."34 + 45"  e visualizza a schermo il risultato
'''
operazione = input("inserisci l'operazione da eseguire :  ")
lista =  operazione.split(" ")
if lista[1] == "+":
    ris = int(lista[0]) + int(lista[2])
if lista[1] == "-":
    ris = int(lista[0]) - int(lista[2])
if lista[1] == "*":
    ris = int(lista[0]) * int(lista[2])
if lista[1] == "/":
    ris = int(lista[0]) / int(lista[2])
print("il risultato dell'operazione  è: ", ris)