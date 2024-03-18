import math

def CalcolaIpotenusa(iLenCateto1,iLencateto2):
    iLenCateto1 =  iLenCateto1 * iLenCateto1
    iLenCateto2 = iLenCateto1 * iLenCateto1
    ilpotenusa = math.sqrt( iLenCateto1 + iLenCateto2 )
    return ilpotenusa

ipotenusa = CalcolaIpotenusa(32,40)
a = 32
b = 40
ipotenusa = CalcolaIpotenusa(a,b)
print(ipotenusa)