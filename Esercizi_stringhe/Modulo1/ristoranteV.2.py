""" 
Gestione di un ristornate, che ci stili i fatturati dei piatti, 
Nel dizionario ci deve essere: costo piatto, portate, nome piatto

"""

def funzione():
    
    piatto1 = {
        "Nome piatto": "Carbanora",
        "Costo piatto": 10,
        "Portate servite": 6 
    }
    
    piatto2 = {
        "Nome piatto": "Matriciana",
        "Costo piatto": 5,
        "Portate servite":  7
    }
    
    fatturatopiatto1 = piatto1.get("Costo piatto") * piatto1.get("Portate servite")
    
    fatturatopiatto2 = piatto2.get("Costo piatto") * piatto2.get("Portate servite")
    
    print(f'Il fatturato della {piatto1.get("Nome piatto")} è {fatturatopiatto1}€')
    print(f'Il fatturato della {piatto2.get("Nome piatto")} è {fatturatopiatto2}')
    
funzione()