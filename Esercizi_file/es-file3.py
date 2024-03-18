def CreaFile(nomFile,frase):
    PathFile = "/home/studente113/File_Progetti_Python" + "/" + nomFile + ".txt"
    f = open(PathFile,"w")
    f.write(frase)
    f.close()
    print(" File creato correttamente")
    
    
while(1):
    print("Programma Principale")
    nome_File = input("scrivi il nome del file : ")
    frase = input(" scrivi il contenuto del file : ")
    CreaFile(nome_File,frase)
