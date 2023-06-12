#Funcao para criar a matriz quadrada
def Cria_matriz(num, lista):
    for i in range (num):
        linha = []
        for j in range(num):
            linha.append(2**(i+j))
        lista.append(linha)
