def menu():
    print("Escolha uma opção:")
    print("1- Ler um arquivo xml")
    print("2- Obter informações do vendedor")
    print("3- Obter informações do cliente")
    print("4- Itens comprado")
    print("5- Valor total da compra")
    print("6- Sair")

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

repetir = True
while(repetir):
    menu()
    opcao = int(input("Digite a opção:"))

    if(opcao == 1):
        pass
    elif(opcao == 2):
        pass
    elif(opcap == 3):
        pass
    elif(opcao == 4):
        pass
    elif(opcao == 5):
        pass
    elif(opcao == 6):
        repetir = False
# Abre e lê o arquivo xml
with open(arquivo, 'rb') as arquivo:
    
    # Converte o arquivo xml e um Dicionário
    documento = xmltodict.parse(arquivo)
    
    #print(documento['nfeProc']['NFe']['infNFe']['det'])
    produtos = documento['nfeProc']['NFe']['infNFe']['det']
    print("Nome dos produtos comprados: \n")
    for item in produtos:
        print(item['prod']['xProd'])
        