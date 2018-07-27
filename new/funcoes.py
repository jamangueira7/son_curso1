from new import ultils
from new import operacoes
from new import operacao_usuario
import getpass

conta_erro = {'erro':{'qtd':0}}

def acessar_conta(opcao_inicial):
    op_conta_sair = True
    ultils.limpar_tela()
    ultils.navegacao_tela(opcao_inicial)

    conta_inicial = input("Digite sua conta:")
    senha = getpass.getpass("Digite sua senha:")

    ultils.limpar_tela()
    if operacao_usuario.logar(conta_inicial, senha):
        erros(True)
        return op_acessar_conta(conta_inicial)
    else:
        print('Conta inválida')
        return erros()

def op_acessar_conta(opcao_inicial):

    while True:
        # Menu de opções
        ultils.opcoes_menu_acessar_conta()
        opcao_CC = input(">>> ")
        # Identificar a tela de navegacação e identificar usuario logado
        ultils.limpar_tela()
        ultils.navegacao_tela(opcao_inicial, opcao_CC)
        #identificarUser()
        if opcao_CC == '11':
            operacoes.mostrar_saldo()
            input(">>> ")
        elif opcao_CC == '12':
            valSaque = input("Digite um valor:")
            operacoes.sacar(int(valSaque),opcao_inicial)
            input(">>> ")
        elif opcao_CC == '13':
            valDeposito = input("Digite um valor:")
            operacoes.depositar(int(valDeposito),opcao_inicial)
            input(">>> ")
        elif opcao_CC == '14':
            conta_transf = input("Digite a conta que receberá a transferencia:")
            valTransferencia = input("Digite um valor:")
            operacoes.transferir(conta_transf, int(valTransferencia),opcao_inicial)
            input(">>> ")
        elif opcao_CC == '9':
            operacao_usuario.deslogar_usuario()
            return True
        else:
            print("Opção inválida")
            operacao_usuario.deslogar_usuario()
            return False

def fazer_deposito():
    while True:
        ultils.limpar_tela()
        # Menu de opções
        ultils.opcoes_menu_deposito()
        opcao_DP = input(">>> ")
        if opcao_DP == '21':
            conta_dep = input("Digite a conta que receberá o deposito:")
            val_dep = input("Digite um valor:")
            operacoes.deposito_sem_logar(conta_dep, int(val_dep))
        elif opcao_DP == '22':
            print("Conta Poupança só pode receber valores ate R$ 200")
            conta_dep = input("Digite a conta que receberá o deposito:")
            val_dep = input("Digite um valor:")
            if int(val_dep) > 200:
                ultils.limpar_tela()
                print("Valor inválida, operação cancelada")
                input(">>> ")
            else:
                operacoes.deposito_sem_logar(conta_dep, int(val_dep))
        elif opcao_DP == '9':
            return True
        else:
            print("Opção inválida")
            return False

def erros(limpar = False):
    if(limpar):
        conta_erro['erro']['qtd'] = 0

    conta_erro['erro']['qtd'] += 1
    if conta_erro['erro']['qtd'] >= 3:
        print("Numero de tentativas acedidas. Programa será encerrado")
        input(">>>")
        return False
    return True