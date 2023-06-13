# Importar a biblioteca que converte um xml em dicionário python
import xmltodict
#observação: é um OrderedDict -> Sempre a mesma ordem
        # Dict -> Não possui ordem definida

# Recebe o nome do arquivo digitado pelo usuário ex: DANFEBrota.xml
arquivo = 'DANFEBrota.xml'#input("Digite o nome do arquivo: ")

# Verifica se o arquivo digitado é um xml
while(arquivo[-3:] != 'xml'):
    arquivo = input("Digite o nome do arquivo: ")
    #observação: existe métodos melhores para verificar se o arquivo é realmente um arquivo xml
    #implementar aqui um método melhor!


# Abre e lê o arquivo xml
with open(arquivo, 'rb') as arquivo:
    
    # Converte o arquivo xml e um Dicionário
    documento = xmltodict.parse(arquivo)
    
    #print(documento['nfeProc']['NFe']['infNFe']['det'])
    produtos = documento['nfeProc']['NFe']['infNFe']['det']
    print("Nome dos produtos comprados: \n")
    for item in produtos:
        print(item['prod']['xProd'])
        