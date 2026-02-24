from flask import Flask, render_template, request


app = Flask(__name__)


# Função para ler usuários do .txt
def carregar_usuarios():

    usuarios = []

    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    user, senha = linha.split(";")
                    usuarios.append({"user": user, "senha": senha})
    except FileNotFoundError:
        with open("usuarios.txt", "w") as arquivo:
            arquivo.write("# usuario;senha\n")

    return usuarios


# Página de login
@app.route("/")
def login():
    return render_template("login.html")

# Página de cadastro
@app.route("/cadastro")
def pagina_cadastro():
    return render_template("cadastro.html")

@app.route("/inicio")
def pagina_inicio():
    return render_template("inicial.html")


# Quando o usuário enviar o formulário
@app.route("/inicio", methods=["POST"])
def entrar():

    usuario_digitado = request.form["usuario"]
    senha_digitada = request.form["senha"]

    usuarios = carregar_usuarios()

    for u in usuarios:
        if usuario_digitado == u["user"] and senha_digitada == u["senha"]:
            return  f"<h1>Bem-vindo, {usuario_digitado}!</h1>"

    return "<h1>Usuário ou senha incorretos</h1>"



@app.route("/cadastro", methods=["POST"])
def cadastrar():

    usuario_novo = request.form["usuario"]
    senha_novo = request.form["senha"]

    usuarios = carregar_usuarios()

    for u in usuarios:
        if usuario_novo == u["user"]:
            return "<h1>Usuário já existente</h1>"
    
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario_novo};{senha_novo}\n")

    return login()

if __name__ == "__main__":
    app.run(debug=True)