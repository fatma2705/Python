# esercizio somma versione 3
# ti chiede quanti numeri vuoi sommare e se sbagli e scrivi un carattere ti da 3 tentativi 
# e poi ti chiede i numri e te li somma 
import sys


def funzione():
    iTentativo = 0
    iNumTentativi = 3
    while(iTentativo<iNumTentativi):
        a = input("Quanti numeri vuoi sommare?")#se mi dice che la variabile non è definita significa che la variabile è
        #dentro un ciclo e il run non passà da lì
        try:
            b = int(a)
            print(f"Hai inserito {a}")
            iTentativo= 100 #abbiamo messo 100 perchè 100>3(iNumTentativi) quindi uscirà dal ciclo while
        except:
            print("Attenzione numero errato")
            iTentativo +=1
            if iTentativo == 3 :
                sys.exit(5) # si può scrivere senza lo zero e si può cambiare il numero
                            #in base al numero che scrivi ti uscirà alla fine codice finito con ("il numero che hai messo")
    somma = 0
    for numeri in range(0,b):
        num = int(input("scrivi il numero"))
        somma = somma + num
    print(f"La somma è {somma} ")


funzione()