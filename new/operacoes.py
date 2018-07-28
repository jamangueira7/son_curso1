from new import ultils
from new import dados_banco
from new import operacao_usuario
from new import arquivo

def mostrar_saldo():
    print("saldo: RS %s" %(operacao_usuario.usuario_logado[0]['valor']))

def sacar(valor, conta_inicial):
    if dados_banco.lista_contas[conta_inicial]['valor'] >= valor:
        dados_banco.lista_contas[conta_inicial]['valor'] -= valor
        print("Saque realizado no valor de R$%s" %valor)
        arquivo.salvar_operacoes_contas()
        mostrar_saldo()
    else:
        print("Operação não realizada: Valor insuficiente")

def depositar(valor,conta_inicial):
    dados_banco.lista_contas[conta_inicial]['valor'] += valor
    print("Deposito realizado no valor de R$%s" % valor)
    arquivo.salvar_operacoes_contas()
    mostrar_saldo()

def transferir(conta,valTransferencia,conta_inicial):
    ultils.limpar_tela()
    ultils.navegacao_tela('1', '14')
    if conta in dados_banco.lista_contas:
        print("Usuario: %s" %dados_banco.lista_contas[conta]['nome'])
        print("Valor: %s" %valTransferencia)
        decisao = input("Aperte 1 para confirmar a transferencia:")
        if decisao == '1' and dados_banco.lista_contas[conta]['valor'] >= valTransferencia:
            print("Transferencia realizada.")
            dados_banco.lista_contas[conta]['valor'] += valTransferencia
            dados_banco.lista_contas[conta_inicial]['valor'] -= valTransferencia
            arquivo.salvar_operacoes_contas()
            mostrar_saldo()
        elif decisao == '1' and dados_banco.lista_contas[conta]['valor'] <= valTransferencia:
            print("Sua conta não tem o valor para transferencia")
        else:
            print("Transferencia cancelada")
    else:
        print("Não encontramos o usuario, por favor tente novamente.")

def deposito_sem_logar(conta,valTransferencia):
    ultils.limpar_tela()
    ultils.navegacao_tela('2')
    if conta in dados_banco.lista_contas:
        print("Usuario: %s" %dados_banco.lista_contas[conta]['nome'])
        print("Valor: %s" %valTransferencia)
        decisao = input("Aperte 1 para confirmar o deposito:")
        if decisao == '1':
            print("Deposito realizado.")
            dados_banco.lista_contas[conta]['valor'] += valTransferencia
            arquivo.salvar_operacoes_contas()
            input(">>> ")
        else:
            print("Deposito cancelado")
    else:
        print("Não encontramos o usuario, por favor tente novamente.")

