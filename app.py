# essa linha e usada para importar
from flask import Flask
#	Cria o aplicativo e guarda em app; __name__ identifica o módulo.
app = Flask(__name__)

#	Associa o endereço inicial à função abaixo.
@app.route("/")
#	Define a função chamada home.
def home():


#	Devolve a mensagem de boas-vindas ao navegador.
    return "Welcome to Valadares Cafe"

#	Associa o endereço /about à função abaixo.
@app.route("/about")
#	Define a função chamada about.
def about():
   #	Devolve a descrição do café ao navegador.
    return "Valadares Cafe is a neighborhood cafe in Miami serving coffee and fresh pastries."
