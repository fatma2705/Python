print("Ciao a tutti-PROGRAMMA4")
a = input("inserisci un numero")
b = input("inserisci un altro numero")
c = input("inserisci l operatore")
a = int(a)
b = int(b)
res = 0
if (c =='+') :
    res = a+b
    descr = "somma"
elif (c =='-') :
    res = a-b
    descr = " sottrazione "
elif (c =='*') :
    res = a*b
    descr = " multiplicazione "
elif (c =='/') :
    res = a/b
    descr = " divisione "
print("La " + descr + " di " + str(a) + " e " + str(b) + " è " + str(res))