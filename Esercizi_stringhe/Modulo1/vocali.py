def frase():
    f = input(" scrivi una frase ")
    a = f.count("a")
    e = f.count("e")
    i = f.count("i")
    o = f.count("o")
    u = f.count("u")
    print(f' nella frase precedente sono presenti {a} a , {e} e ,{i} i , {o} o , {u} u ')
    if f.find("python") > -1:
        print(f' la frase precedente contiene la parola "python" ')
    else:
        print(f'la frase precedente non contiene la parola "python" ')
    if f.find("basta") > -1:
        return False
    else:
        return True

continua = True

while continua:
    continua = frase()

