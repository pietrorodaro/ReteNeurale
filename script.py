# COSTANTI
FEATURES = 5 #Definiamo il numero di criteri per prendere la decisione in questo caso 5
THRESHOLD = 0.5 #Valore costante utile per la decisione, se il calcolo restituirà più di 0.5 ci fara andare al concerto

#Funzione di attivazione
def activation(x):
    if x > THRESHOLD: #Se x è maggiore della soglia restituiamo 1=andare al concerto altrimento 0=non andare al concerto
        return 1
    else:
        return 0

#carichiamo i pesi dal file    
def carica_pesi(filename, weights):
    try: #Usiamo try per cercare eventuali errori
        file = open(filename, "r")
    except FileNotFoundError:
        print(f"Errore: file{filename} non trovato!") #Segnialiamo l' errore
        return 0, 0.0
    
    lines = file.readlines() #Leggiamo tutto il file e lo memorizziamo in un array

    for i in range(FEATURES):
        valore_peso= float(lines[i].split(':')[1]) #Prendiamo la riga corrente la diviamo a metà con i due punti e convertiamo il valore in decimale
        weights.append(valore_peso) #Aggiugniamo il valore appena ottenuto dal file nella lista 'weights'
        
        bias= float(lines[FEATURES].split(':')[1]) #Sempre dalla stessa riga otteniamo anche il valore del bias e lo convertiamo in decimale
        file.close()

    return 1, bias #Restituiamo 1(operazione svolta con successo) e il bias

def prevedi(weights, bias, input_array):
    somma=bias #Creiamo una variabile somma che parte dal valore del bias

    for i in range (FEATURES):
        somma += input_array[i] * weights[i] #Prendiamo l' input lo moltiplichiamo per il suo peso e lo aggiungiamo alla somma

        return activation(somma) #Passiamo la somma finale alla funzione activation 
    
def main():
    weights = [] #Creiamo una lista vuota

    successo, bias = carica_pesi("pesi_concerto.txt", weights) # Chiamiamo la funzione e salviamo i risultati

    if not successo:
        return 1 # Ferma il programma e restituisce 1
    
    print("Inserisci i dati:") 
    input_array = [0] * FEATURES # Prepariamo l'array dove salvare le risposte

    input_array[0] = int(input("Artista famoso? (1=Si, 0=No): ")) # E salviamo la risposta

    input_array[1] = int(input("Bel meteo? (1=Si, 0=No): ")) # E salviamo la risposta

    input_array[2] = int(input("Amici presenti? (1=Si, 0=No): ")) # E salviamo la risposta

    input_array[3] = int(input("Cibo buono? (1=Si, 0=No): ")) # E salviamo la risposta

    input_array[4] = int(input("Alcol disponibile? (1=Si, 0=No): ")) # E salviamo la risposta

    decisione = prevedi(weights, bias, input_array) # Calcoliamo la decisione tramite funzione (sarà o 1 o 0)

    if decisione: # In base alla decisione mando la risposta
        print("\n Vai al concerto! \n")
    else:
        print("\n Resta a casa \n")

    return 0

main()

