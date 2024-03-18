'''
scrivere un programma che chiede all'utente il titolo della pagina , il testo centrale e il testo interno 
e con questi 3 input crei automaticamente una pagina html
'''
Nfile = input(" inserisci il nome del file ")
Tpagina = input(" scrivi il titolo della pagina html")
Tcentrale = input(" scrivi il testo centrale della pagina html")
Tinterno = input(" scrivi il testo interno della pagina html")
sPathFile = "/home/studente113/Scrivania/python/Recupero"
NomeFile = sPathFile + "/" + Nfile + ".html"
ContenutoFile = "<html>" + "\n" + "<head>" + "\n" 
Cfile = "<title>" + "\n" + Tpagina + "\n" + "</title>" + "\n" + "</head>"
cFile =  "\n" + "<body>" + "\n" + "<center><h1>" + Tcentrale + "</h1></center>" + "\n" 
sFile =  Tinterno + "\n" + "</body>" + "\n" + "</html>"
f = open(NomeFile,"w")
f.write(ContenutoFile)
f.write(Cfile)
f.write(cFile)
f.write(sFile)
f.close 
print("il file è stato creato")
    
