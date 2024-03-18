def Somma(num1,num2,num3,num4,num5):
    somma = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
    return somma 


def SommaNum(NumUtente):
    somma = 0
    for i in range(0,NumUtente):
        num1 = input(" Inserisci il numero : ")
        somma += int(num1)
    return somma 





print("Programma Principale ")
n1 = input("scrivi un numero :")
n2 = input("scrivi un altro numero :")
n3 = input("scrivi un altro numero :")
n4 = input("scrivi un altro numero :")
n5 = input("scrivi un altro numero :")
totale = Somma(n1,n2,n3,n4,n5)
print(f" La somma totale dei numeri inseriti è {totale}")
nUtente = int(input(" Quanti numeri vuoi sommare ? "))
STotale = SommaNum(nUtente)
print(f" la somma totale dei {nUtente} inseriti è {STotale}")