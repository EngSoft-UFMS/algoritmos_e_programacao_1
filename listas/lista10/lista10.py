# Resolução do exercício 1
lista = list(map(int, input().split()))
numinserido, posicao = map(int, input().split())

lista.insert(posicao, numinserido)
print(lista)

# Resolução do exercício 2
lista = list(map(int, input().split()))
posicao = int(input())

print(lista[posicao])
lista.pop(posicao)
print(lista)
