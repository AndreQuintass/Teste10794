from Banco import Conta

#Criação das contas e outras variaveis
ContasBancarias: list[Conta] = [Conta(1, "Andre Quintas", 200), Conta(2, "Joao Santos", 1000)]
usingAccount: Conta = None
dia = 1

#Muda a conta a ser utilizada
def usarConta(conta: Conta):
    global usingAccount
    usingAccount = conta
    print("Conta a ser utilizada: " + conta.nome_proprietario)

#Loop principal da aplicação
def acao():
    global dia, usingAccount
    while True:
        print()
        try:
            escolha = int(input("Selecione uma opção:"
                                "\n  1 - Criar Conta"
                                "\n  2 - Selecionar Conta"
                                "\n  3 - Levantar dinheiro"
                                "\n  4 - Depositar dinheiro"
                                "\n  5 - Transferir dinheiro para conta"
                                "\n  6 - Consultar extrato da conta"
                                "\n  7 - Sair"
                                "\n  (8 - Passar para o proximo dia)"
                                "\n Opcao: "))
        except:
            print("\n!!Erro de valores!!\n")
            continue

        match escolha:
            case 1:
                nome = input("Insira o nome da sua conta: ")
                try:
                    dinheiro = int(input("Insira a quantidade de dinheiro inicial: "))
                    if dinheiro < 0:
                        raise Exception("Erro de valores")
                except:
                    print("\n!!Erro de valores!!\n")
                    continue
                ContasBancarias.append(Conta(nome_proprietario=nome, dinheiro=dinheiro))
            case 2:
                for i in range(len(ContasBancarias)):
                    print(f"{i+1} - {ContasBancarias[i]}")
                try:
                    escolha = int(input("Opcao: "))-1
                    usarConta(ContasBancarias[escolha])
                except:
                    print("\n!!Erro de valores!!\n")
                    continue
            case 3:
                if usingAccount == None:
                    print("!!Selecione uma conta primeiro!!")
                    continue
                try:
                    quant = int(input("Quantidade para levantar: "))
                    if quant <= 0:
                        raise Exception("Erro de valores")
                    usingAccount.levantar(quant)
                except:
                    print("\n!!Erro de valores!!\n")
                    continue
            case 4:
                if usingAccount == None:
                    print("!!Selecione uma conta primeiro!!")
                    continue
                try:
                    quant = int(input("Quantidade para depositar: "))
                    if quant <= 0:
                        raise Exception("Erro de valores")
                    usingAccount.depositar(quant)
                except:
                    print("\n!!Erro de valores!!\n")
                    continue
            case 5:
                if usingAccount == None:
                    print("!!Selecione uma conta primeiro!!")
                    continue
                if len(ContasBancarias) <= 1:
                    print("!!Não existem outras contas!!")
                    continue
                outrasContas = ContasBancarias[:]
                outrasContas.remove(usingAccount)
                for i in range(len(outrasContas)):
                    print(f"{i+1} - {outrasContas[i]}")
                try:
                    escolha = int(input("Para quem deseja enviar o dinheiro?: "))-1
                    quant = int(input("Quantidade para enviar: "))
                    if quant <= 0:
                        raise Exception("Erro de valores")
                    usingAccount.enviar(quant, outrasContas[escolha])
                except:
                    print("\n!!Erro de valores!!\n")
                    continue

            case 6:
                if usingAccount == None:
                    print("!!Selecione uma conta primeiro!!")
                    continue
                if len(usingAccount.extrato) == 0:
                    print("Não existem registos")
                    continue
                for registo in usingAccount.extrato:
                    print(registo)

            case 7:
                print("Obrigado por escolher o nosso banco :)")
                return 0

            case 8:
                dia += 1
                for conta in ContasBancarias:
                    conta.resetDiario()
                print("\nDia atual: " + str(dia))

            case _:
                print("\n!!Erro de valores!!\n")
                continue


acao()