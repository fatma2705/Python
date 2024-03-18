def funzione():
    dizionario = {'A': 1, 'B': 14, 'C': 24, 'D': 23, 'E': 4, 'F': 2,
                  'G': 8, 'H': 13, 'I': 15, 'J': 21, 'K': 22, 'L': 17, 'M': 6,
                  'N': 18, 'O': 10, 'P': 9, 'Q': 11, 'R': 16, 'S': 3, 'T': 7,
                  'U': 19, 'V': 25, 'W': 12, 'X': 5, 'Y': 20, 'Z': 26, " " : " " }
    a = input("scrivi una frase in maiuscolo ")
    l = []
    for carattere in a:
        b = str(dizionario[carattere])
        l.append(b)
    risultato = " ".join(l)
    print(f" la frase {a} dopo che è stata  codificata è diventata {risultato}")


funzione()