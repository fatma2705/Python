def ContaVocali(stringa):
    vocali = ["a","e","i","o","u"]
    num_vocali = 0
    for carattere in stringa:
        if carattere in vocali :
            num_vocali += 1
    return num_vocali
    
def ContaVocaliFile(stringa):
    pathFile = "/home/studente113/Documenti" + "/" + "ParoleTanteVocali" + ".txt"
    path_File = "/home/studente113/Documenti" + "/" + "ParolePocheVocali" + ".txt"
    inum = ContaVocali(stringa)
    if inum > 2 :
        f = open(pathFile,"a") 
        f.write(stringa)
        f.close()
    else:
        f = open(path_File,"a") 
        f.write(stringa)
        f.close()
   
        
while(1):
    parola =input(" scrivi una parola :") 
    ContaVocaliFile(parola)