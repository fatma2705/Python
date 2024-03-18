def numero():
    n = int(input("scrivi un numero "))
    n1 = int(input("scrivi un altro numero "))
    if n > n1:
        print(f' il numero {n} è maggiore di {n1}')
    else:
        print(f'il numero {n} è minore di {n1}')

numero()