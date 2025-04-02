listaSpesa = []

def Aggiungi(Elemento):
    listaSpesa.append(Elemento)

def Visualizza():
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")

def Rimuovi(Elemento):
    if Elemento > 1 or Elemento < len(listaSpesa):
        listaSpesa.pop(Elemento)
    else:
        print("Elemento non valido")

x = 1

print("Benvenuto nella lista della spesa!")
print("Scrivi 0 per uscire")
print("Scrivi 1 per aggiungere un elemento")
print("Scrivi 2 per visualizzare la lista")
print("Scrivi 3 per rimuovere un elemento")

while x != 0:
    x = int(input("Cosa vuoi fare? "))
    if x == 1:
        Elemento = input("Scrivi l'elemento da aggiungere: ")
        Aggiungi(Elemento)
    elif x == 2:
        Visualizza()
    elif x == 3:
        Elemento = int(input("Scrivi il numero dell'elemento da rimuovere: ")) - 1
        Rimuovi(Elemento)
    elif x == 0:
        print("Arrivederci!")
    else:
        print("Comando non valido")
