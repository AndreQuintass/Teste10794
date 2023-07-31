from fastapi import FastAPI
from Banco import Conta

app = FastAPI()

#Criação das contas e outras variaveis
ContasBancarias: list[Conta] = [Conta(1, "Andre Quintas", 200), Conta(2, "Joao Santos", 1000)]
usingAccount: Conta = None
dia = 1


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




