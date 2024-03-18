'''
procedura che ritorna un booleano a seconda se soper è fatta bene oppure no 
soper = "45 + 78" #sequenza spazio operatore spazio sequenza 
'''

def Verifica_Operazione(operazione):
    lista = operazione.split(" ")
    num = "1234567890"
    for elemento in lista[0] :
        if elemento not in num:
            return False
    if lista[1] != "+" or lista[1] != "-" or lista[1] != "*" or lista[1] != "/":
        return False
    for i  in lista[2]:
        if i not in num: 
            return False
    return True


while(1):
    operazione = input("inserisci l'operazione da eseguire :  ")
    ris = Verifica_Operazione(operazione)
    if ris is False:
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
    else:
        print(" Stringa inserita errata")