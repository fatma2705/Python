'''
scrivere un programma che chiede all'utente nome,cognome,codice fiscale
e salva i dati su un file che si trova nella cartella home/utenti e che
si chiama il codice fiscale dell'utente + ".dat " 
'''
import sys

#creare una funzione che fa la stessa cosa di len()
def lunghezza(stringa):
    num_caratteri = 0
    for i in stringa:
        num_caratteri +=1
    return num_caratteri

def VerificaCodiceFiscale(stringa):
    stringa.lower()
    lettere = "qwertyuioplkjhgfdsazxcvbnm"
    for i in lettere :
        for a in range(0,6):
            if stringa[a] in i  and lunghezza(stringa) == 16 :
                return 1
    else:
        return 0
    
# secondo metodo per verficare il codice fiscale
def secondaVerificaCodiceFiscale(stringa):
    if lunghezza(stringa) == 16 :
        for i in range(0,6):
            if stringa.lower()[i]<= 'a' and stringa.lower()[i]>='z':
                return 0
        else:
            return 1
    else:
        return 0 
    

def DatiUtente(Nome,Cognome,CodiceFiscale):
    verifica =VerificaCodiceFiscale(CodiceFiscale)
    if verifica == 1:
        StringaUtente = "nome:" + Nome + ";" + "cognome:" + Cognome + ";" + "codice_fiscale:" + str(CodiceFiscale)
        PathFile = "/home/studente113/Scrivania/python/Lezioni Recupero/Utenti"
        NomeFile = PathFile + "/" + CodiceFiscale + ".dat"
        f = open(NomeFile,"w")
        f.write(StringaUtente)
        f.close()
    else: 
        print("il codice fiscale inserito è errato")
        sys.exit()
        



print("Programma Principale ")
nome = input(" inserisci il tuo nome ")
cognome = input(" inserisci il tuo cognome ")
codice_fiscale = input(" inserisci il tuo codice fiscale ")
Stringa_Utente = DatiUtente(nome,cognome,codice_fiscale)
print(" il file è stato creato e salvato correttamente dentro la cartella (Utenti) ") 
