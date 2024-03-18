def Somma(num1,num2,num3,num4,num5):
    somma = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
    return somma 

def InserisciNumeri(n1,n2,n3,n4,n5):
    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    lista.append(n4)
    lista.append(n5)
    return lista

print("Programma Principale ")
n1 = input("scrivi un numero :")
n2 = input("scrivi un altro numero :")
n3 = input("scrivi un altro numero :")
n4 = input("scrivi un altro numero :")
n5 = input("scrivi un altro numero :")
totale = Somma(n1,n2,n3,n4,n5)
print(f" La somma totale dei numeri inseriti è {totale}")
totale = InserisciNumeri(n1,n2,n3,n4,n5)
print(f" La lista dei numeri inseriti è {totale}")

