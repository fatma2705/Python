# esrcizio somma  versione 1 scrivi quanti numeri nuoi sommare e poi scrivi i numeri da sommare e te li somma

def funzione():
    a = input("Quanti numeri vuoi sommare?")
    a1 = int(a)
    somma = 0
    for numeri in range(0,a1):
        num = int(input("scrivi il numero"))
        somma = somma + num
    print(f"La somma è {somma} ")


funzione()