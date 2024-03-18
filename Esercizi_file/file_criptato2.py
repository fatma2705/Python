def CrittoCesare(sStringa,Chiave):
    sStringaCriptata = ""
    for elemento in sStringa:
        iNuovoCodice = ord(elemento) + Chiave
        if iNuovoCodice > 122:
            iNuovoCodice = 65 + iNuovoCodice - 122 - 1
        char = chr(iNuovoCodice)
        sStringaCriptata = sStringaCriptata + char
    return sStringaCriptata

def FileCripatato(nFile,stringa,chiave):
    StringaCriptata = CrittoCesare(stringa,chiave)
    PathFile = "/home/studente113/Documenti" + "/" + nFile + ".txt"
    f = open(PathFile,"w")
    f.write(StringaCriptata)
    f.close()
    
    
print(" Programma Principale")
NomeFile = input(" inserisci il nome del file nuovo :")
Stringa = input(" inserisci la frase da criptografare : ")
chiave = int(input("inserisci la chiave criptografia :"))
ris = FileCripatato(NomeFile,Stringa,chiave)
print(" file creato e salvato correttamente ")