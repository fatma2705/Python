#esercizio somma versione 2
#ti chiede quanti numeri vuoi sommare
#  se per sbaglio metti un carattere ti dice che non hai scritto
#  un numero e te lo ristituisce con il numero 5
import sys


def funzione():
    a = input("Quanti numeri vuoi sommare?")
    try:
        a1 = int(a)
        print(f"Hai inserito {a}")
    except:
        print("Attenzione numero errato")
        a1 = 5
    somma = 0
    for numeri in range(0,a1):
        num = int(input("scrivi il numero"))
        somma = somma + num
    print(f"La somma è {somma} ")


funzione()