def CrittoCesare(sStringa,Chiave):
    sStringaCriptata = ""
    for elemento in sStringa:
        iNuovoCodice = ord(elemento) + Chiave
        if iNuovoCodice > 122:
            iNuovoCodice = 65 + iNuovoCodice - 122 - 1
        char = chr(iNuovoCodice)
        sStringaCriptata = sStringaCriptata + char
    return sStringaCriptata
        

def FileCrittato(PathFile,Chiave):
    f = open(PathFile,"r")
    sStringa = f.read()
    f.close()
    sStringaCriptata = CrittoCesare(sStringa,Chiave)
    f = open(PathFile,"w")
    f.write(sStringaCriptata)
    f.close()
    return sStringaCriptata

    
print(" Programma Principale")


PathFile = input("  inserisci il path del file da cripttografare :")
ris = FileCrittato(PathFile,7)
print("il contenuto del file passato è stato cripttato correttamente ")
print(ris)
# /home/studente113/Documenti/frase_criptografata.txt
