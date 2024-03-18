import sys
def VerificaNumero(StringaDaVerificare):
    for car in StringaDaVerificare:
        if((car<'0' or car>'9') and (car!= '.')):
            return 1
        return 0
NumTentativi = 0
while(NumTentativi <3):
    a = input("inserisci un numero ")
    b = input("inserisci un numero ")
    if(VerificaNumero(a)==0 and VerificaNumero(b)==0):
        a = int(a)
        b = int(b)
        c = a +b
        print("ok")
        sys.exit()
    else:
        NumTentativi +=1
        print(" Attenzione ,inseriti caratteri non numeri ")