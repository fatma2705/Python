def funzione():
    import random
    a = (random.randrange(1,10))
    b = (random.randrange(1,10))
    c = input(f"quanto fa {a} x {b} ?")
    z = int(a) * int(b) 
    if int(c) == int(z) > -1:
        print(" hai risposto correttamente ")
    else:
        print(" non hai risposto correttmente ") 

funzione()


