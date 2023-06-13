import math

def calcular_total_impostos(n):
    # Encontra o maior divisor de N
    maior_divisor = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            maior_divisor = max(maior_divisor, i)

    # Calcula o total mínimo de impostos
    total_impostos = n // maior_divisor
    return total_impostos
