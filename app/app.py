# Importazione delle librerie necessarie
from flask import Flask,render_template

# Creazione dell'applicazione Flask
app = Flask(__name__)

# Definizione di una variabile da passare al template
x = "ciao"

# Definizione della route principale (homepage)
@app.route('/')
def index():
    # Rendering del template index.html passando la variabile x rinominata come 'paperino'
    return render_template('index.html', paperino=x)

# Blocco che permette di eseguire l'app direttamente da questo file
# con il debug attivato per visualizzare gli errori durante lo sviluppo
if __name__ == '__main__':
    app.run(debug=True)