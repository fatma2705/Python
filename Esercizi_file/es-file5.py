'''
scrivere un programma che chiede all'utente un percorso e scrive in output :
- se il percorso esiste 
- quanti file ci sono 
- quanti file ci sono che finiscono con una estensione 
'''
import os 
import sys

def PathExists(PathAssoluto):
    numdirectory = 0
    numfiles = 0
    numfilepy = 0
    numfiletxt = 0
    numfilepdf = 0
    if os.path.isfile(PathAssoluto) == True:
        print("il path passato è il percoraso di un file \n" )
        sys.exit()
    elif os.path.isdir(PathAssoluto) == True:
        print(" il path passato è il percorso di una directory \n")
    else:
        print(" il path passato è il percorso di un file/directory che non esiste   \n")
        sys.exit()
    for elemento in os.scandir(PathAssoluto):
        if  os.path.isfile(elemento):
                numfiles += 1 
        if os.path.isdir(elemento):
            numdirectory += 1 
    for files in os.listdir(PathAssoluto):
        if  os.path.isfile(elemento):
                if files.endswith(".py"):
                    numfilepy += 1
                if files.endswith(".txt"):
                    numfiletxt += 1
                if files.endswith(".pdf"):
                    numfilepdf += 1
    print(f" nel Path passato sono presenti {numdirectory} sottocartelle ,{numfiles}file di cui {numfilepy} python files , {numfiletxt} txt files e {numfilepdf} pdf files")


        
print(" Programma Principale")
Path = input("scrivi il path di una directory  per verificare l'esistenza : ")
PathExists(Path)