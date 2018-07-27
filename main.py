from new import ultils
from new import funcoes
from new import arquivo
#from new import gerar_banco

continuar = True

def main():
    arquivo.carregar_contas()
    ultils.apresentacao()
    opcao_inicial = ultils.opcoes_menu_inicial()

    if opcao_inicial == '1':
        # OPÇÃO CONTA CORRENTE
        return funcoes.acessar_conta(opcao_inicial)

    elif opcao_inicial == '2':
        # OPÇÃO DEPOSITO SEM LOGAR
        return funcoes.fazer_deposito(opcao_inicial)

    else:
        return funcoes.sair()

while continuar:
    continuar = main()



