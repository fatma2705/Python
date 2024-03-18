def ristorante():

    caciopepe = input("quante cacio e pepe sono state servite ? ")
    prezzocaciopepe = input("qual è il prezzo della cacio e pepe ? ")

    totalecaciopepe =  int(caciopepe) *  int(prezzocaciopepe) 
    
    matriciana = input("quante matriciane sono state servite ? ")
    prezzomatriciana = input("quante matriciane sono state servite ?")

    totalematriciana = int(matriciana) * int(prezzomatriciana) 
    
    totale =  totalecaciopepe + totalematriciana

    print(f' il fatturato della cacio e pepe è {totalecaciopepe}')
    print(f' il fatturato della matriciana è {totalematriciana}')
    print(f' il fatturato totale è {toatale}')

ristorante()