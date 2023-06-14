def cria_matriz(linhas, colunas):
    matriz = []
    for _ in range(linhas):
        linha = list(map(float, input().split()))
        matriz.append(linha)
    return matriz

def soma_lin(matriz, linha):
    if linha < 0 or linha >= len(matriz):
        return "Linha inválida."

    resultado = sum(matriz[linha])
    return resultado

def med_lin(matriz, linha):
    if linha < 0 or linha >= len(matriz):
        return "Linha inválida."

    resultado = sum(matriz[linha]) / len(matriz[linha])
    return resultado

def soma_col(matriz, coluna):
    if coluna < 0 or coluna >= len(matriz[0]):
        return "Coluna inválida."

    resultado = sum(matriz[i][coluna] for i in range(len(matriz)))
    return resultado

def media_col(matriz, coluna):
    if coluna < 0 or coluna >= len(matriz[0]):
        return "Coluna inválida."

    resultado = sum(matriz[i][coluna] for i in range(len(matriz))) / len(matriz)
    return resultado

def soma_diagonal1(matriz):
    resultado = sum(matriz[i][i] for i in range(len(matriz)))
    return resultado

def med_diagonal1(matriz):
    resultado = sum(matriz[i][i] for i in range(len(matriz))) / len(matriz)
    return resultado

def soma_diagonal2(matriz):
    resultado = sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))
    return resultado

def med_diagonal2(matriz):
    resultado = sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz))) / len(matriz)
    return resultado

def imprimir(soma_lin, med_lin, soma_col, media_col,soma_diagonal1, med_diagonal1,soma_diagonal2, med_diagonal2):
  
    print("Soma da linha:", soma_lin)

    print("Média da linha:", med_lin)

    print("Soma da coluna:", soma_col)

    print("Média da coluna:", media_col)

    print("Soma da diagonal principal:", soma_diagonal1)

    print("Média da diagonal principal:", med_diagonal1)

    print("Soma da diagonal secundária:", soma_diagonal2)

    print("Média da diagonal secundária:", med_diagonal2)

linhas = int(input("linhas da matriz: "))
colunas = int(input("colunas da matriz: "))

matriz = cria_matriz(linhas, colunas)

linha = int(input("linha que deseja calcular: "))
coluna = int(input("coluna que deseja calcular: "))

soma_lin = soma_lin(matriz, linha)

med_lin = med_lin(matriz, linha)

soma_col = soma_col(matriz, coluna)

media_col = media_col(matriz, coluna)

soma_diagonal1 = soma_diagonal1(matriz)

med_diagonal1 = med_diagonal1(matriz)

soma_diagonal2 = soma_diagonal2(matriz)

med_diagonal2 = med_diagonal2(matriz)

imprimir(soma_lin, med_lin, soma_col,media_col, soma_diagonal1,med_diagonal1, soma_diagonal2,med_diagonal2)
