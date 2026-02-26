from flask import request, render_template

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



def cadastrar():

    usuario_novo = request.form["usuario"]
    senha_novo = request.form["senha"]

    usuarios = carregar_usuarios()

    for u in usuarios:
        if usuario_novo == u["user"]:
            return render_template("cadastro.html", fail_2=True)
    
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{usuario_novo};{senha_novo}\n")

    return render_template("login.html")


def entrar():

    usuario_digitado = request.form["usuario"]
    senha_digitada = request.form["senha"]

    user = (f"Bem vindo, {usuario_digitado}!")

    usuarios = carregar_usuarios()

    for u in usuarios:
        if usuario_digitado == u["user"] and senha_digitada == u["senha"]:
            return render_template("inicial.html", message=user)

    return render_template("login.html", fail=True)