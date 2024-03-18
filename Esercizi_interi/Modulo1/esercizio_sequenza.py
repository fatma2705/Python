from random import randint
def funzione():
    sequenza = [1,2,3,4]
    sequenzaDaIndovinare = []
    for i in range(4):
        sequenzaDaIndovinare.append(sequenzaDaIndovinare)


    while len(sequenza) > 0:
        selezionare = randint(0, 9)
        numero = sequenza.pop(selezionare)
        sequenzaDaIndovinare.append(numero)

        print(f"indovina la sequenza dei numeri da 1 a 4")

        numero1 = int(input(" "))
        numero2 = int(input(" "))
        numero3 = int(input(" "))
        numero4 = int(input(" "))

        if numero1 == sequenzaDaIndovinare [0] and numero2 == sequenzaDaIndovinare [1] and numero3 == sequenzaDaIndovinare [2] and numero4 == sequenzaDaIndovinare  [3]:
            print(f"le hai indovinate tutte correttamente")
            return False

        if numero1 != sequenzaDaIndovinare  [0] and numero2 != sequenzaDaIndovinare [1] and numero3 != sequenzaDaIndovinare  [2] and numero4 != sequenzaDaIndovinare [3]:
            print (f"non le hai indovinate correttamente ")
            return True

        if numero1 == sequenzaDaIndovinare [0]:
            print(f" il numero {numero1} è nella posizione giusta ")
        if numero2 == sequenzaDaIndovinare  [1]:
            print(f" il numero {numero2} è nella posizione giusta ")
        if numero3 == sequenzaDaIndovinare [2]:
             print(f" il numero {numero3} è nella posizione giusta ")
        if numero4 == sequenzaDaIndovinare  [3]:
            print(f" il numero {numero4} è nella posizione giusta ")

        print(f"i numeri erano ({sequenzaDaIndovinare }")
continua = True
while continua:
    continua = funzione()