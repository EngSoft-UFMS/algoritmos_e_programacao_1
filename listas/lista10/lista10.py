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

# Resolução do exercício 3
tam = int(input())
lista = []


cont = 1
verif = 0

while cont <= tam:
    num = int(input())
    lista.append(num)
    cont = cont + 1

numpverif = int(input())

for i in range(tam):
    if lista[i] == numpverif:
        print('sim')
    else: 
        verif = verif + 1
        
if verif == tam:
    print('não')
    
# Resolução do exercício 4
prodalcool = list(map(float, input().split()))
somasemana = 0

for i in range(len(prodalcool)):
    somasemana = somasemana + prodalcool[i]

print(f'{somasemana:.2f}')


