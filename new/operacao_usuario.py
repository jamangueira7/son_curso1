from new import dados_banco
from new import arquivo

usuario_logado = []

def logar(conta_inicial, senha):
    if conta_inicial in dados_banco.lista_contas and senha == dados_banco.lista_contas[conta_inicial]['senha']:
        arquivo.criar_arquivo_usuario_logado(dados_banco.lista_contas[conta_inicial],conta_inicial)
        usuario_logado.append(dados_banco.lista_contas[conta_inicial])
        return True
    else:
        return False

def identificar_usuario():
    print("Usuario logado: %s" %(usuario_logado[0]['nome']))

def deslogar_usuario():
    arquivo.apagar_usuario_logado()

def mostrar_usuario_logado():
    return arquivo.ler_arquivo_usuario_logado()