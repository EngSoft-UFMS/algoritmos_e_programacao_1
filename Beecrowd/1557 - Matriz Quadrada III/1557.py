#Funcao para criar a matriz quadrada
def Cria_matriz(num, lista):
    for i in range (num):
        linha = []
        for j in range(num):
            linha.append(2**(i+j))
        lista.append(linha)
        
#Funcao para imprimir a matriz
def Imprime_matriz(num, lista):
    T = len(str(lista[num-1][num-1]))
    for i in range(num):
        for j in range(num):
            lista[i][j] = str(lista[i][j])
            while len(lista[i][j]) < T:
                lista[i][j] = ' ' + lista[i][j]
        M = ' '.join(lista[i])

        print(M)
    print()

#Chamada das funcoes
num = int(input())
while(num!=0):
    lista = []
    Cria_matriz(num, lista)
    Imprime_matriz(num, lista)
    num = int(input())
