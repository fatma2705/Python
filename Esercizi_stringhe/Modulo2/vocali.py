'''
scrivere una funzione che passata una stringa ci da come output il numero di vocali che contiene questa stringa 
'''

def ContaVocali(stringa):
    num_vocali = 0
    stringa = stringa.lower()
    vocali = ["a","e","i","o","u","à","è","ì","ò","ù"]
    for i in stringa :
        if i in vocali :
            num_vocali += 1
    return num_vocali
        




print("programma principale")
Stringa = input(" scrivi una parola: ")
tot_vocali = ContaVocali(Stringa)
print(f" la parola {Stringa} contiene {tot_vocali} vocali ")
        