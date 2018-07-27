import os

def apresentacao ():
    print("****************************************")
    print("*** School of net - Caixa Eletrônico ***")
    print("****************************************")


def opcoes_menu_inicial():
    print("1 - Acessar sua conta")
    print("2 - Fazer um deposito")
    print("9 - Sair")
    return input("Digite a opção >>> :")

def opcoes_menu_acessar_conta():
    print("*** 1 - Acessar Conta ***")
    print("11 - Saldo")
    print("12 - Saque")
    print("13 - Deposito")
    print("14 - Transferencia")
    print("9 - Sair")

def opcoes_menu_deposito():
    print("*** 2 - Deposito ***")
    print("21 - Conta corrente")
    print("22 - Conta poupança")
    print("9 - Sair")

def navegacao_tela(op_inicial, op_interna = None):
    msg = ""
    if op_inicial == '1':
        msg = "1 - Conta Corrente"
    elif op_inicial == '2':
        msg = "2 - Conta Corrente"

    if op_interna != None:
        msg += " - Opção Interna %s" %op_interna
    print(msg)

def limpar_tela():
    limpar = 'cls' if os.name == 'nt' else 'clear'
    os.system(limpar)