from flask import Flask, render_template
from funcoes import cadastrar, entrar

app = Flask(__name__)

############################ PÁGINAS ######################
# Página de login
@app.route("/")
def login():
    return render_template("login.html")

# Página de cadastro
@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")

# Página de início
@app.route("/inicio")
def pagina_inicio():
    return render_template("inicial.html")

#Função de Login para Início
@app.route("/inicio", methods=["POST"])
def func_entrar():
    return entrar()

#Função de Cadastro para Login
@app.route("/cadastro", methods=["POST"])
def func_cadastro():
    return cadastrar()


if __name__ == "__main__":
    app.run(debug=True)