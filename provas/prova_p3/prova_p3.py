


### Exercicio 1

##Programa: erva-mate-pantaneira.py
# Programador: Wagner Rodrigues
# Data: 28/11/2022
#projete e implemente um programa para ler duas matrizes m x n, m,n > 0, a e b, calcular c, a soma das matrizes,
#e imprimir c, onde cada elemento da matriz c é dado por: ci,j=ai,j+

## passo 1 ler tamanho da lista de Campo Grande
tamcampo = int(input())

## passo 1.1 ler todos os valores de Campo Grande
campo = list(map(int, input().split()))[:tamcampo]
##passo 1.2 Ler tamanho da lista Ponta Porã
tamponta = int(input())
## passo 1.3 Ler todos os valores de Ponta Porã
ponta = list(map(int, input().split()))[:tamponta]

## passo 2 iniciar a uniao dos valores de Campo Grande
u = campo
# ## passo 3 "para todos os valores em ponta" 
for valores in ponta:
## passo 3.1 descobrir os valores de Ponta Porã que tem em Campo grande 
   if valores not in u:
## passo 4  inserir os valores na uniao 
      u.append(valores)

## passo 5 imprimir valores da lista uniao 
print(u)






### Exercicio 2


##Programa: calculo.py
# Programador: Wagner Rodrigues
# Data: 28/11/2022
#projete e implemente um programa para ler duas matrizes m x n, m,n > 0, a e b, calcular c, a soma das matrizes,
#e imprimir c, onde cada elemento da matriz c é dado por: ci,j=ai,j+bi,j

### passo 1 receber os valores de cada linha e coluna 
linhas, colunas  = map(int, input().split())
## passo 1.1 Organizar cada valor da linha 
a = [0]*linhas
b = [0]*linhas
c = [0]*linhas
## passo 2 "para todo i em alcance de linhas" posicionar as suas respectivas colunas
for i in range(linhas):
    a[i] = [0]*colunas
    b[i] = [0]*colunas
    c[i] = [0]*colunas

## passo 3 inserir valores de a em suas respectivas linhas
for i in range (linhas):
    a[i] = list(map(int, input().split()))

## passo 3.1 inserir valores de b em suas respectivas linhas
for i in range (linhas):
    b[i] = list(map(int, input().split()))
      
## passo 4 percorer linhas e colunas 
for i in range (linhas):
    for j in range(colunas):
## passo 5 na matriz c sera o resultado da soma de aij + bij 
        c[i][j] =  a[i][j]+ b[i][j]

# passo 6 imprimir o resultado para cada lista que c calcular
for i in range(len(c)):
    print(c[i])






### Exercicio 3


# -*- coding: utf-8 -*-
# Programa: temperatura02.py
# Programador: Wagner Rodrigues
# Data: 28/11/2022
# Este programa lê um conjunto de temperaturas lidas em determinados locais
# durante os dias da semana, computa e imprime a temperatura média em
# cada um dos locais. As medidas são tomadas diariamente, em 
# determinados horários e em determinados locais. 


## passo 1 criar uma matrix 4x3: 4 linhas e 3 colunas
temperatura = [[0.0]*3 for _ in range(4)]
## passo 2. somar cada linha e coluna em suas respectivas posicoes:
for  i in range(0,4):
    temperatura[i] = list(map(float,input().split())) 
## passo 2. somar cada linha e coluna em suas respectivas posicoes:
# obs decidi implementar a soma dessa maneria para o codigo ficasse mais compreencivel o possivel 
# de maneira que qualquer pessoa , possa interpretar o codigo
soma1 = temperatura[0][0] + temperatura[1][0] + temperatura[2][0] + temperatura[3][0]
soma2 = temperatura[0][1] + temperatura[1][1] + temperatura[2][1] + temperatura[3][1]
soma3 = temperatura[0][2] + temperatura[1][2] + temperatura[2][2] + temperatura[3][2]
## passo 3. calcular as medias de cada soma
media1 = soma1/4.0
media2 = soma2/4.0
media3 = soma3/4.0
# passo 4. Imprimir o resultado de cada media 
print(f'1  {media1:.1f}')
print(f'2  {media2:.1f}')
print(f'3  {media3:.1f}')

