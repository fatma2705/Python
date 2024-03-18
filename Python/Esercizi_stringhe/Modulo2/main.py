'''
in un ciclo while chiedete all'utente una frase e stampate 
.lunghezza frase
.numero parole 
. numero lettere
''' 

while True :
    Nlettere = 0
    frase = input("Scrivi una frase :  (o scrivi 'stop' se hai finito)")
    if frase.lower() == "stop":
                break
    lunghezza = len(frase)
    Nparole = len(frase.split(" "))
    lettere = "qwertyuioplkjhgfdsazxcvbnm"
    for i in frase.lower() :
        if i in lettere :
            Nlettere += 1
    print(f" La lunghezza della frase inserita è {lunghezza} , contiene {Nparole} parole e {Nlettere} lettere  ")
            
            
        
    