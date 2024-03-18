'''
chiedi all'utente di inserire una stringa e stampa le posizioni delle vocali 
'''
stringa = input("scrivi una frase :  ")
vocali = "aeiou"
pos = 0
for i in stringa:
    if i in vocali:
       print(f" la frase {stringa} contiene la vocale {i} nella posizione {pos}")
    pos = pos + 1