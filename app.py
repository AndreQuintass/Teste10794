import flask
from flask import Flask
from Banco import Conta

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

ContasBancarias: list[Conta] = [Conta(4, "Andre Quintas", 200),
                                Conta(5, "Joao Santos", 1000)]
usingAccount: Conta = None
dia = 1


@app.route('/')
def hello_world():
    return flask.render_template("index.html",
                                 lista=ContasBancarias,
                                 dia=dia)

@app.route('/conta/<id>')
def htmlConta(id: int):
    global usingAccount
    for account in ContasBancarias:
        if account.id == int(id):
            acc = account
    usingAccount = acc
    othersList = ContasBancarias[:]
    othersList.remove(acc)
    return flask.render_template("indexAluno.html",
                                 lista=ContasBancarias,
                                 conta=acc,
                                 othersList=othersList)


@app.route('/criarconta', methods=["POST"])
def criarconta():
    nome = flask.request.form['novoNome']
    dinheiro = int(flask.request.form['Dinheiro'])
    novaConta = Conta(nome_proprietario=nome, dinheiro=dinheiro)
    ContasBancarias.append(novaConta)

    return flask.redirect("/")

@app.route('/levantar', methods=["POST"])
def levantar():
    if usingAccount == None:
        return flask.redirect("/")
    dinheiro = int(flask.request.form['Dinheiro'])
    if dinheiro < 0:
        return flask.redirect("/conta/" + str(usingAccount.id))
    usingAccount.levantar(dinheiro)
    return flask.redirect("/conta/" + str(usingAccount.id))


@app.route('/depositar', methods=["POST"])
def depositar():
    if usingAccount == None:
        return flask.redirect("/")
    dinheiro = int(flask.request.form['Dinheiro'])
    if dinheiro < 0:
        return flask.redirect("/conta/" + str(usingAccount.id))
    usingAccount.depositar(dinheiro)
    return flask.redirect("/conta/" + str(usingAccount.id))

@app.route('/enviar', methods=["POST"])
def enviar():
    if usingAccount == None:
        return flask.redirect("/")
    id_pessoa = int(flask.request.form['id_pessoa'])
    dinheiro = int(flask.request.form['Dinheiro'])
    if dinheiro < 0:
        return flask.redirect("/conta/" + str(usingAccount.id))
    for account in ContasBancarias:
        if account.id == id_pessoa:
            acc = account
    usingAccount.enviar(dinheiro, acc)
    return flask.redirect("/conta/" + str(usingAccount.id))

@app.route('/passardia', methods=["POST"])
def passardia():
    global dia
    dia += 1
    return flask.redirect("/")

@app.route('/voltar', methods=["POST"])
def voltar():
    return flask.redirect("/")


if __name__ == '__main__':
    app.run()



























"""
@app.get("/")
async def root():
    return {"message": "Bem vindo"}


@app.get("/contas/")
async def showContas():
    if len(ContasBancarias):
        return ContasBancarias
    else:
        return "Não existem contas"


@app.get("/contas/add/")
async def addContas(nome: str, dinheiro: int):
    if dinheiro < 0:
        return "Erro dinheiro tem que ser positivo"
    ContasBancarias.append(Conta(nome_proprietario=nome, dinheiro=dinheiro))
    return "Successo"

@app.get("/contas/choose")
async def chooseContas(id: int):
    for account in ContasBancarias:
        if account.id == id:
            acc = account
    global usingAccount
    usingAccount = acc
    return "Conta a ser utilizada: " + usingAccount.nome_proprietario

@app.get("/banco/levantar")
async def getMoney(dinheiro: int):
    if usingAccount == None:
        return "!!Selecione uma conta primeiro!!"
    if dinheiro < 0:
        return "Erro dinheiro tem que ser positivo"
    return usingAccount.levantar(dinheiro)

@app.get("/banco/depositar")
async def depositMoney(dinheiro: int):
    if usingAccount == None:
        return "!!Selecione uma conta primeiro!!"
    if dinheiro < 0:
        return "Erro dinheiro tem que ser positivo"
    return usingAccount.depositar(dinheiro)

@app.get("/banco/transfer")
async def sendMoney(id: int, dinheiro: int):
    if usingAccount == None:
        return "!!Selecione uma conta primeiro!!"
    if len(ContasBancarias) <= 1:
        return "!!Não existem outras contas!!"
    outrasContas = ContasBancarias[:]
    outrasContas.remove(usingAccount)
    if dinheiro < 0:
        return "Erro dinheiro tem que ser positivo"
    for account in ContasBancarias:
        if account.id == id:
            acc = account
    return usingAccount.enviar(dinheiro, acc)

@app.get("/banco/checkRegistry")
async def checkRegistry():
    if usingAccount == None:
        return "!!Selecione uma conta primeiro!!"
    if len(usingAccount.extrato) == 0:
        return "Não existem registos"
    return usingAccount.extrato

@app.get("/passardia")
async def passardia():
    global dia
    dia += 1
    for conta in ContasBancarias:
        conta.resetDiario()
    return "Dia atual: " + str(dia)

@app.get("/sair")
async def sair():
    return "Obrigado por escolher o nosso banco :)"
"""