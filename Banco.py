from random import randint
from datetime import datetime

#Limites
limiteOneTime = 500
limiteDiario = 2500


class Conta:
    def __init__(self, id: int = randint(1, 999999999), nome_proprietario: str = "NOME SOBRENOME", dinheiro: int = 0):
        self.id = id
        self.nome_proprietario = nome_proprietario
        self.dinheiro = dinheiro
        self.extrato = []
        self.quantDiaria = 0

    def __str__(self):
        return f"{self.nome_proprietario}, Dinheiro: {self.dinheiro}"

    def __repr__(self):
        return f"{self.nome_proprietario}"

    def levantar(self, quantidade: int):
        if quantidade <= self.dinheiro and quantidade <= limiteOneTime and quantidade + self.quantDiaria <= limiteDiario:
            self.quantDiaria += quantidade
            self.dinheiro -= quantidade
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.extrato.append(f"{current_time} - {self.nome_proprietario} levantou {quantidade} e ficou com {self.dinheiro} na conta.")
            return "Successo"
        else:
            return "!!Quantidade Invalida!!"

    def depositar(self, quantidade: int):
        self.dinheiro += quantidade
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.extrato.append(f"{current_time} - {self.nome_proprietario} depositou {quantidade} e ficou com {self.dinheiro} na conta.")
        return "Successo"

    def enviar(self, quantidade: int, conta: 'Conta'):
        if quantidade <= self.dinheiro:
            self.dinheiro -= quantidade
            conta.dinheiro += quantidade
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.extrato.append(f"{current_time} - {self.nome_proprietario} enviou {quantidade} para {conta.nome_proprietario} e ficou com {self.dinheiro} na conta.")
            conta.extrato.append(f"{current_time} - {conta.nome_proprietario} recebeu {quantidade} de {self.nome_proprietario} e ficou com {conta.dinheiro} na conta.")
            return "Successo"
        else:
            return "!!Quantidade Invalida!!"

    def resetDiario(self):
        self.quantDiaria = 0
