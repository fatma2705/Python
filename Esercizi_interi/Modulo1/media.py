def media(*numeri: float):
    tot = 0
    for num in numeri:
        tot += num
    media = tot / len(numeri)
    print(media)
    return media

media(2.3,1.6,2.1,4.1,7,9)
media(2.3,4.1,7,9)
media(2.3,1.6,2.1,4.1,7,9,11,3.2)

print("inserire i numeri tra cui fare la media, scrivere = alla fine")
continua = True
numeri = []
while continua:
    numero = input("aggiungi un numero")
    if numero == "=":
        continua = False
    else:
        numeri.append(float(numero))

print(f'La media è: {media(*numeri)}')