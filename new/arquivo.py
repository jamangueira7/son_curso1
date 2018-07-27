import os
from new import dados_banco

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

#USUARIO_LOGADO
def abrir_arquivo_usuario_logado(mode):
    return open(BASE_PATH + '/_user_logado.dat', mode)

def criar_arquivo_usuario_logado(usuario,conta):
    arquivo = abrir_arquivo_usuario_logado('w')
    escrever_arquivo_usario_logado(arquivo,usuario,conta)
    arquivo.close()

def ler_arquivo_usuario_logado(arquivo):
    linha = arquivo.readline()
    usuario ={}
    for dados in linha:
        usuario = {
                dados[0] : {
                'nome':dados[1],
                'senha':dados[2],
                'valor':int(dados[3]),
                'tipo':dados[4],
            }
        }
    return usuario

def apagar_usuario_logado():
    arquivo = abrir_arquivo_usuario_logado('w')
    arquivo.write("")
    arquivo.close()

def escrever_arquivo_usario_logado(arquivo,usuario,conta):
        arquivo.write(
            conta +';'+
            usuario['nome']+';'+
            usuario['senha']+';'+
            str(usuario['valor'])+';'+
            usuario['tipo']+';'
        )

#CONTAS
def abrir_arquivo_contas(tipo):
    return open(BASE_PATH + '/_contas_banco.dat', tipo)

def criar_arquivo_contas():
    arquivo = abrir_arquivo_contas('w')
    escrever_arquivo_contas(arquivo)
    arquivo.close()

def escrever_arquivo_contas(arquivo):
    for conta,dados_conta in dados_banco.lista_contas.items():
        arquivo.writelines((
            conta, ';',
            dados_conta['nome'],';',
            dados_conta['senha'],';',
            str(dados_conta['valor']),';',
            dados_conta['tipo'],';',
            '\n'
        ))
def ler_arquivo_contas(arquivo):
    linhas = arquivo.readlines()
    for contas in linhas:
        montar_contas(contas)

def montar_contas(contas):
    dados_conta = []
    while contas.find(';') != -1:
        semicolon_pos = contas.find(';')
        data = contas[0:semicolon_pos]
        dados_conta.append(data)
        if semicolon_pos + 1 == len(contas):
            break
        else:
            contas = contas[semicolon_pos+1:len(contas)]
    add_contas(dados_conta)

def add_contas(dados_conta):
    dados_banco.lista_contas[dados_conta[0]] = {
            'nome':dados_conta[1],
            'senha':dados_conta[2],
            'valor':float(dados_conta[3]),
            'tipo': dados_conta[4],
        }

def carregar_contas():
    arquivo = abrir_arquivo_contas('r')
    ler_arquivo_contas(arquivo)
    arquivo.close()

def salvar_operacoes_contas():
    arq = abrir_arquivo_contas('w')
    escrever_arquivo_contas(arq)
    arq.close()
