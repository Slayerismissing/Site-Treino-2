from flask import Flask, render_template, request, session, redirect
from app import usuario
import bcrypt

app = Flask(__name__)
app.secret_key = ("algo_muito_creepy")

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
@app.route("/login", methods=["GET","POST"])
def func_entrar():
    
    email = request.form["email"]
    senha = request.form["senha"]

    email_encontrado = usuario.find_one({"email":email})

    if not email_encontrado:
        return redirect("/inicio", error=True)
    
    senha_hash = email_encontrado["senha"]

    if bcrypt.checkpw(senha.encode("utf-8"), senha_hash):
        session["usuario_nome"] = email_encontrado["email"]
        return redirect("/inicio")
    else:
        return redirect("/", error=True)
    
    

#Função de Cadastro para Login
@app.route("/cadastro", methods=["POST"])
def func_cadastro():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        email_encontrado = usuario.find_one({"email":email})

        if email_encontrado:
            return redirect("/cadastro", error=True)


        senha_bytes = senha.encode("utf-8")
        senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())

        usuario.insert_one({
            "email":email,
            "senha":senha_hash
        })

        return redirect("/")
    return redirect("/cadastro")


if __name__ == "__main__":
    app.run(debug=True)