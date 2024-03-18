a = input("inserisci primo numero: ")
b = input("inserisci secondo numero: ")
c = int(a)/int(b)
print("il risultato della divisione è",c)

# questa è una funzione che è fissa
def EseguiDivisione(dividendo,divisore):
    c = dividendo/divisore
    return c
# dati della funzione
a = input("inserisci primo numero: ")
b = input("inserisci secondo numero: ")
ris =EseguiDivisione( int(a),int(b))
print("il risultato della divisione è",ris)