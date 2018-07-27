from new import arquivo

def carregar_banco():
    carregar_dados_conta('a')

def carregar_dados_conta(tipo):
    arq = arquivo.abrir_arquivo_contas(tipo)
    arquivo.escrever_arquivo_contas(arq)
    arq.close()

carregar_banco()