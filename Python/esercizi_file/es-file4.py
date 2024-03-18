import datetime 
def file() :
    pathFile = "/home/studente113/Scrivania" + "/" + str(today) + ".txt" 
    f = open(pathFile,"a")
    for i in range (0,5):
        frase = input(" scrivi una frase ")
        today = datetime.date.today()
        f.write(frase + "\n" )
    f.close 
                    


file()



def lettera(destinatario,numFrasi,città):
    today = datetime.date.today()
    giorno = today.day
    mese = today.month
    anno = today.year
    data = str(giorno) + "/" + str(mese) + "/" + str(anno)
    pathFile = "/home/studente113/File_Progetti_Python" + "/" + "lettera per " + destinatario + ".txt"
    f = open(pathFile,"w")
    f.write(città.upper())
    f.write(str(data))
    for i in range (0,numFrasi):
        frase = input(" scrivi  le frasi :")
        f.write("\n" + frase)
    f.write("\n"+"\t" +"\t" + "\t"+"\t"+"\t")
    f.write("Firma :")
    f.close()
    
    
destinatario = input("scrivi il destinatario :")
numFrasi = int(input(" Quante frasi vuoi scrivere :"))
città = input(" scrivi la tua città  :  ")
lettera(destinatario,numFrasi,città)

