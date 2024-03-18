def frase():
    a = input("scrivi una frase")
    b = a.lower()
    c = a.capitalize()
    d = a.swapcase()
    h = a.upper()
    f = a.title()
    j = a.center(180)

    q = a.replace( "e","W")
    k = a.strip()
    print(f" la frase {a} è diventata {b} usando il metodo lower")
    print(f" la frase {a} è diventata {c} usando il metodo capitalize")
    print(f" la frase {a} è diventata {d} usando il metodo swapcase")
    print(f" la frase {a} è diventata {h} usando il metodo upper")
    print(f" la frase {a} è diventata {j} usando il metodo center")
    print(f" la frase {a} è diventata {q} usando il metodo replace")
    print(f" la frase {a} è diventata {k} usando il metodo strip")


frase()
