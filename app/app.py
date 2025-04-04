# Importazione delle librerie necessarie
from flask import Flask,render_template,request,redirect,url_for

# Creazione dell'applicazione Flask
app = Flask(__name__)

lista = ["pasta", "riso", "tonno", "passata di pomodoro", "olive", "maionese"]  # Inizializzazione della lista vuota

# Definizione della route principale (homepage)
@app.route('/')
def index():
    # Rendering del template index.html passando la variabile x rinominata come 'paperino'
    return render_template('index.html', lista=lista)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista.append(elemento)
    return redirect(url_for('index'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return redirect(url_for('index'))

@app.route('/svuota', methods=['POST'])
def rimuovi_tutto():
    lista.clear()
    return redirect(url_for('index'))

# Blocco che permette di eseguire l'app direttamente da questo file
# con il debug attivato per visualizzare gli errori durante lo sviluppo
if __name__ == '__main__':
    app.run(debug=True)