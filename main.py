import getpass
import os

usuarioLogado = []
opcaoInicial = None
contaErro = 0

listaContas = {
        '0001-01': {
            'senha': '123456',
            'nome': 'Fulano de Tal',
            'valor': 1000,
            'tipo': 'adm'
        },
        '0002-02': {
            'senha': '654321',
            'nome': 'Beltrano Silva',
            'valor': 800,
            'tipo': 'cp'
        },
        '0003-03': {
            'senha': '654321',
            'nome': 'Beltrano Silva',
            'valor': 800,
            'tipo': 'cc'
        }
}

def apresentacao ():
    print("****************************************")
    print("*** School of net - Caixa Eletrônico ***")
    print("****************************************")

def opcoesMenuInicial():
    print("1 - Acessar sua conta")
    print("2 - Fazer um deposito")
    print("9 - Sair")

def opcoesMenuAcessarConta():
    print("*** 1 - Acessar Conta ***")
    print("11 - Saldo")
    print("12 - Saque")
    print("13 - Deposito")
    print("14 - Transferencia")
    print("9 - Sair")

def opcoesMenuDeposito():
    print("*** 2 - Deposito ***")
    print("21 - Conta corrente")
    print("22 - Conta poupança")
    print("9 - Sair")

def logar(contaInicial, senha):
    if contaInicial in listaContas and senha == listaContas[contaInicial]['senha']:
        usuarioLogado.append(listaContas[contaInicial])
        return True
    else:
        return False

def limparTela():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)

def navegacaoTela(opInicial, opInterna = None):
    msg = ""
    if opInicial == '1':
        msg = "1 - Conta Corrente"
    elif opInicial == '2':
        msg = "2 - Conta Corrente"

    if opInterna != None:
        msg += " - Opção Interna %s" %opInterna
    print(msg)

def identificarUser():
    print("Usuario logado: %s" %(usuarioLogado[0]['nome']))
def deslogarUser():
    usuarioLogado.clear()
    limparTela()

def mostrarSaldo():
    print("saldo: RS %s" %(usuarioLogado[0]['valor']))

def sacar(valor):
    if listaContas[contaInicial]['valor'] >= valor:
        listaContas[contaInicial]['valor'] -= valor
        print("Saque realizado no valor de R$%s" %valor)
        mostrarSaldo()
    else:
        print("Operação não realizada: Valor insuficiente")

def deposito(valor):
    if usuarioLogado:
        listaContas[contaInicial]['valor'] += valor
        print("Deposito realizado no valor de R$%s" % valor)
        mostrarSaldo()
    else:
      print("teset")

def transferencia(conta,valTransferencia):
    limparTela()
    navegacaoTela('1', '14')
    if conta in listaContas:
        print("Usuario: %s" %listaContas[conta]['nome'])
        print("Valor: %s" %valTransferencia)
        decisao = input("Aperte 1 para confirmar a transferencia:")
        if decisao == '1' and listaContas[conta]['valor'] >= valTransferencia:
            print("Transferencia realizada.")
            listaContas[conta]['valor'] += valTransferencia
            listaContas[contaInicial]['valor'] += valTransferencia
            input(">>> ")
        elif decisao == '1' and listaContas[conta]['valor'] <= valTransferencia:
            print("Sua conta não tem o valor para transferencia")
        else:
            print("Transferencia cancelada")
    else:
        print("Não encontramos o usuario, por favor tente novamente.")

def depositoSemLogar(conta,valTransferencia):
    limparTela()
    navegacaoTela('2')
    if conta in listaContas:
        print("Usuario: %s" %listaContas[conta]['nome'])
        print("Valor: %s" %valTransferencia)
        decisao = input("Aperte 1 para confirmar o deposito:")
        if decisao == '1':
            print("Deposito realizado.")
            listaContas[conta]['valor'] += valTransferencia
            input(">>> ")
        else:
            print("Deposito cancelado")
    else:
        print("Não encontramos o usuario, por favor tente novamente.")


sair = True

while sair:
    apresentacao()

    if opcaoInicial == None:
        opcoesMenuInicial()
        opcaoInicial = input(">>> ")

    if opcaoInicial == '1':

        #OPÇÃO CONTA CORRENTE
        opContaSair = True
        limparTela()
        navegacaoTela(opcaoInicial)
        contaInicial = input("Digite sua conta:")
        senha = getpass.getpass("Digite sua senha:")
        limparTela()
        if logar(contaInicial, senha):
            contaErro = 0
            while opContaSair:
                # Menu de opções
                opcoesMenuAcessarConta()
                opcaoCC = input(">>> ")
                #Identificar a tela de navegacação e identificar usuario logado
                limparTela()
                navegacaoTela(opcaoInicial, opcaoCC)
                identificarUser()
                if opcaoCC == '11' :
                    mostrarSaldo()
                    input(">>> ")
                elif opcaoCC == '12' :
                    valSaque = input("Digite um valor:")
                    sacar(int(valSaque))
                    input(">>> ")
                elif opcaoCC == '13':
                    valDeposito = input("Digite um valor:")
                    deposito(int(valDeposito))
                    input(">>> ")
                elif opcaoCC == '14':
                    conta_transf = input("Digite a conta que receberá a transferencia:")
                    valTransferencia = input("Digite um valor:")
                    transferencia(conta_transf, int(valTransferencia))
                    input(">>> ")
                elif opcaoCC == '9':
                    deslogarUser()
                    opContaSair = False
                    opcaoInicial = None
                else:
                    contaErro += 1
                    print("Opção inválida")
                    if contaErro >= 3:
                        deslogarUser()
                        opContaSair = False
                        opcaoInicial = None
        else:
            contaErro +=1
            print('Conta inválida')
            if contaErro >= 3:
                deslogarUser()
                sair = False

    elif opcaoInicial == '2':

        #OPÇÃO DEPOSITO SEM LOGAR
        opDepositoSair = True
        contaErro = 0
        while opDepositoSair:
            limparTela()
            # Menu de opções
            opcoesMenuDeposito()
            opcaoDP = input(">>> ")
            if opcaoDP == '21':
                contaDep = input("Digite a conta que receberá o deposito:")
                valDep = input("Digite um valor:")
                depositoSemLogar(contaDep,int(valDep))
            elif opcaoDP == '22':
                print("Conta Poupança só pode receber valores ate R$ 200")
                contaDep = input("Digite a conta que receberá o deposito:")
                valDep = input("Digite um valor:")
                if int(valDep) > 200:
                    limparTela()
                    print("Valor inválida, operação cancelada")
                    input(">>> ")
                else:
                    depositoSemLogar(contaDep, int(valDep))
            elif opcaoDP == '9':
                deslogarUser()
                opDepositoSair = False
                opcaoInicial = None
            else:
                contaErro += 1
                print("Opção inválida")
                if contaErro >= 3:
                    deslogarUser()
                    opDepositoSair = False
                    opcaoInicial = None

    else:
        sair = False



