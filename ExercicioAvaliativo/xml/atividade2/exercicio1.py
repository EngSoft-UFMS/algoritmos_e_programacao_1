def menu():
    print(".+****+.Escolha uma opção.+****+.")
    print("1- Ler um arquivo xml")
    print("2- Obter informações do vendedor")
    print("3- Obter informações do cliente")
    print("4- Itens comprado")
    print("5- Valor total da compra")
    print("6- Sair")
    print(".+****+..+****+..+****+..+****+.")

# Importar a biblioteca que converte um xml em dicionário python
import xmltodict




repetir = True
while(repetir):
    menu()
    opcao = int(input("Digite a opção:"))
    print("\n\n")

    if(opcao == 1):
        # Recebe o nome do arquivo digitado pelo usuário ex: DANFEBrota.xml
        arquivo = 'DANFEBrota.xml'#input("Digite o nome do arquivo: ")

        # Verifica se o arquivo digitado é um xml
        while(arquivo[-3:] != 'xml'):
            arquivo = input("Digite o nome do arquivo: ")
            
    elif(opcao == 2):
        with open(arquivo, 'rb') as arq:
            documento = xmltodict.parse(arq)
            print("CNPJ:{:} ".format(documento['nfeProc']['NFe']['infNFe']['emit']['CNPJ']))
            print("Nome:{:} ".format(documento['nfeProc']['NFe']['infNFe']['emit']['xNome']))
            print("Nome Fantasia:{:} ".format(documento['nfeProc']['NFe']['infNFe']['emit']['xFant']))
            print("Rua:{:}, {}".format(documento['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xLgr'], documento['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['nro']))
            print("Bairro:{:} ".format(documento['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xBairro']))
            print("Município:{:}-{} ".format(documento['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['xMun'], documento['nfeProc']['NFe']['infNFe']['emit']['enderEmit']['UF']))
            print("\n\n")
    elif(opcao == 3):
        with open(arquivo, 'rb') as arq:
            documento = xmltodict.parse(arq)
            print("CPF:{:} ".format(documento['nfeProc']['NFe']['infNFe']['dest']['CPF']))
            print("Nome:{:} ".format(documento['nfeProc']['NFe']['infNFe']['dest']['xNome']))
            print("Rua:{:}, {}".format(documento['nfeProc']['NFe']['infNFe']['dest']['enderDest']['xLgr'], documento['nfeProc']['NFe']['infNFe']['dest']['enderDest']['nro']))
            print("Bairro:{:} ".format(documento['nfeProc']['NFe']['infNFe']['dest']['enderDest']['xBairro']))
            print("Município:{:}-{} ".format(documento['nfeProc']['NFe']['infNFe']['dest']['enderDest']['xMun'], documento['nfeProc']['NFe']['infNFe']['dest']['enderDest']['UF']))
            print("\n\n")
    elif(opcao == 4):
        with open(arquivo, 'rb') as arq:
            documento = xmltodict.parse(arq)
            produtos = documento['nfeProc']['NFe']['infNFe']['det']
            print("Nome dos produtos comprados: \n")
            for item in produtos:
                print(item['prod']['xProd'])
            print("\n\n")
    elif(opcao == 5):
        print("Valor Total da Compra: {}".format(documento['nfeProc']['NFe']['infNFe']['total']['ICMSTot']['vNF']))
        print("\n\n")
    elif(opcao == 6):
        repetir = False

        