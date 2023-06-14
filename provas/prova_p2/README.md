Nesta prova, 10% da nota da questão será relativa à documentação do programa.

# Exercício 1-
Projete e implemente um programa para ler dois vetores a e b, representados por duas listas, calcular a soma c =a +b das duas listas e imprimir o resultado c.

Considerando que os vetores têm n elementos cada, representados pelas listas a e b, tem a soma representada pela lista c dada por:

Soma das listas
a = [a[0], a[1], ..., a[n-1]]
b = [b[0], b[1], ..., b[n-1]]

c = [a[0]+b[0], a[1]+b[1], ..., a[n-1]+b[n-1]]

A entrada é dada por um fluxo em duas linhas, cada uma delas com n elementos cada, representado as listas de entrada. A saída consiste em imprimir a lista resultante da soma das duas listas que representam os dois vetores. Neste programa não pode ser utilizada nenhuma função ao método que some diretamente duas listas.

## Exemplo:

formato da entrada

20 17 23 24 15 18 22 21 24 19 21 15 24 24 16

18 17 21 22 25 22 14 17 28 21 33 27 16 17 22

formato da saída

[38, 34, 44, 46, 40, 40, 36, 38, 52, 40, 54, 42, 40, 41, 38]

## Exemplo:

formato da entrada

101 105 120 140 170 123 145 149 155 142 117 167

181 165 133 148 169 124 155 122 123 134 144 177

formato da saída

[282, 270, 253, 288, 339, 247, 300, 271, 278, 276, 261, 344]

# Exercício 2-

Projete e implemente um programa que leia uma lista L de tam >= 2 números inteiros e verifique se os elementos da lista estão em ordem decrescente. O programa deverá imprimir 'verdadeiro' se os elementos da lista estiverem em ordem decrescente ou ' falso' caso contrário. Obeserve que o seguinte predicado pode ser usado para descrever a propriedade se os elementos de L estiverem em ordem decrescente:

∀ i ∈ {0,…,tam−2} : L[i] > L[i+1]

A entrada é dada por uma linha contendo uma lista de tam >= 2 números inteiros. A saída consiste em imprimir 'verdadeiro' se a lista estiver em ordem decrescente e 'falso' caso contrário.

![image](https://github.com/EngSoft-UFMS/algoritmos_e_programacao_1/assets/127704416/27756671-73d1-4a41-b818-9245a38ac3ba)

# Exercício 3-

A Companhia de Erva Mate Pantaneira mantém dois depósitos, um em Campo Grande e outro em Ponta Porã. Cada um com estoques de no máximo 25 itens diferentes. Os produtos são identificados com um número de 3 dígitos. Projete e implemente um programa que leia os números dos produtos dos itens armazenados no depósito em Campo Grande e armazene-os na lista cgr, e então repita este procedimento para os itens armazenados no depósito de Ponta Porã, armazenando esses números de produtos na lista pmg. O programa deve então encontrar e imprimir a interseção dessas duas listas os números dos produtos, isto é, a coleção de números de produtos que estão simultaneamente nos dois depósitos. Os elementos da lista da interseção devem aparecer na mesma ordem que ocorrem na lista de produtos do depósito de Campo Grande. Os estoques não devem ser assumidos como tendo o mesmo número de itens.

A entrada é dada por um fluxo de duas linhas, onde a primeira linha contém tam1 inteiros representando os números dos itens do depósito em Campo Grande e a segunda linha os tam2 inteiros representando os números dos itens do depósito de Ponta Porã. Pode ocorrer da entrada ser uma linha vazia. A saída consiste em escrever a lista resultante da interseção das listas dos itens que estão em ambos os depósitos. No caso da interseção ser vazia, imprima a lista vazia [].

## Exemplo:

formato da entrada

101 103 110 201 225 267 854 876 910 911

101 105 110 117 202 224 267 854 877 901 902 911

formato da saída

[101, 110, 267, 854, 911]

## Exemplo:

formato da entrada

116 333 555

777 888 999 110 111

formato da saída

[]

# Exercício 4-

Uma string é denominada palíndromo quando ela lida do início para o final tem o mesmo significado se a ordem dos caracteres é lida do final para o início. Por exemplo:

![image](https://github.com/EngSoft-UFMS/algoritmos_e_programacao_1/assets/127704416/0abd1806-289a-422c-87da-ce8d2dc17ed9)

são palíndromos.

Projete e implemente um programa para ler uma string de caracteres e então determinar se ela é um palíndromo. Caracteres maiúsculos e minúsculos de um mesmo símbolo são considerados diferentes. A string pode ter caracteres espaço.

A entrada é dada por por um fluxo numa linha contente caracteres do alfabeto latino e o caractere espaço. As strings não possuem dois caracteres espaço juntos. A saída consiste em imprimir para a string da entrada a mensagem se ela é palíndromo ou não.

Neste exercício não pode ser usado nenhuma função ou módulo para manipular blocos da string nem slicing. Só pode ser utilizado a manipulação e concatenação de 'caracteres' e comparação de strings. Podem ser utilizados os métodos string.upper() e string.lower().

Sugestão: Compute a inversa da string usando um laço de repetição.

![image](https://github.com/EngSoft-UFMS/algoritmos_e_programacao_1/assets/127704416/f8672b6e-a320-45d0-8c75-3e27cdfc7b03)


