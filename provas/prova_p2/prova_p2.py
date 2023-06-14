### Exercício 1

# Programa: somavetorial.py
# Programador:Jerfferson Jorge Felizardo Júnior
# Data: 19/10/2022
# Este programa le dois vetores a⃗  e b⃗ representados por duas listas, calcula a soma c⃗ = a⃗ +b⃗  das duas listas e imprime o resultado c⃗ .
# início do módulo principal

#Passo 1 Lê os dois vetores
#Passo 1.1 Lê o vetor a
vetor1 = list(map(int, input().split()))
#Passo 1.2 Lê o vetor b
vetor2 = list(map(int, input().split()))
#Passo 1.3 Cria o vetor c com uma lista vazia
vetor3 = []
#Passo 1.4 Compute o tamanho das listas
tam = len(vetor1)
#Passo 2 Realiza a soma de cada instância de a com b
for i in range (tam):
    vetor3.append(vetor1[i]+vetor2[i])
#Passo 3 Imprime o vetor c resultante
print(vetor3)



### Exercício 2

# Programa: ordemdecrescente.py
# Programador:Jerfferson Jorge Felizardo Júnior
# Data: 19/10/2022
# Este programa le uma lista L de tam >= 2 números inteiros e 
#verifica se os elementos da lista estão em ordem decrescente.

#Passo 1 Lê a lista L
lista = list(map(int, input().split()))
#Passo 1.1 Verifica o tamanho da lista L
tam = len(lista)
#Passo 1.2 Inicializa a mensagem
msg = 'verdadeiro'

#Passo 2 Verifique se os elementos estão em ordem decrescente
for i in range(tam-1):
    if lista[i] <= lista[i+1]:
        msg = 'falso'
        break
#Nesse caso o break poupa a memória que seria gasta caso fosse uma lista imensa com o último 
#valor ocasionando em falso, impedindo o comando de dar seguimento (achou um falso, parou)

#Passo 3 Imprime a msg que diz se é ou não uma lista decrescente
print(msg)



### Exercício 3

# Programa: verifprodutos.py
# Programador:Jerfferson Jorge Felizardo Júnior
# Data: 19/10/2022
# Este programa lê os números dos produtos dos itens armazenados em dois depósitos,um em Campo Grande (cgr) e outro
# em Ponta Porã (pmg). O programa deve então encontrar e imprimir a interseção dessas duas listas os números dos 
# produtos, isto é, a coleção de números de produtos que estão simultaneamente nos dois depósitos.

# Passo 1 Lê a lista dos produtos de Campo Grande
cgr = list(map(int, input().split()))
# Passo 1.1 Verifica o tamanho da lista cgr
tam1 = len(cgr)
# Passo 1.2 Lê a lista dos produtos de Ponta Porã
pmg = list(map(int, input().split()))
# Passo 1.3 Verifica o tamanho da lista pmg
tam2 = len(pmg)
# Passo 1.4 Cria a lista de interseção
intersecao = []

# Passo 2 Compute os produtos existentes nas duas listas

# Resolução feita verificando se o produto em estoque cgr contem o produto comparado no estoque pmg

# Passo 2.1 Para cada produto no estoque de Campo Grande
for produto in cgr:
    #Passo 2.2 Verifica se o mesmo produto também está no estoque de Ponta Porã
    if produto in pmg:
        # Passo 2.3 Se o produto está contido nos dois estoques, adiciona-o na intersecao
        intersecao.append(produto)

# Passo 3 Printa a lista dos produtos existentes nos dois estoques
print(intersecao)



### Exercício 4

# Programa: verifpalindromo.py
# Programador:Jerfferson Jorge Felizardo Júnior
# Data: 19/10/2022
# Este programa lê um uma string de caracteres e então determina se ela é um palíndromo. 
# Caracteres maiúsculos e minúsculos de um mesmo símbolo são considerados diferentes. A string pode ter caracteres 
# espaço.

# Passo 1 Lê a string
string = input()
# Passo 1.1 Transforma suas caracteres para um tamanho igual
string.upper()
# Passo 1.2 Computa o tamanho da string
tam = len(string)

# Passo 2 Cria uma lista vazia para armazenar a string inversa e verificar se a string é um palindromo
inversa = []

# Passo 2.1 Transforma a string em sua inversa
i = 1
while i <= tam:
    inversa.append(string[tam-i])
    i = i + 1

# Passo 2.2 Computa se a string é igual a sua inversa
aux = 0
for i in range(tam):
    if string[i] == inversa[i]:
        aux = aux + 1      
        
# Passo 2.3 Verifica se a variavel utilizada para contar os caracteres iguais tem o mesmo tamanho da string, 
# confirmando se a mesma é ou não palíndromo
if aux == tam:
    # Passo 3 Printar o resultado
    print('palíndromo')
else:
    print('não palíndromo')
