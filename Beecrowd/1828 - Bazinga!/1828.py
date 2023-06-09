# Função para verificar a reação dos jogadores Sheldon e Raj no jogo pedra, papel e tesoura
def verificar_reacao_sheldon(escolha_sheldon, escolha_raj):
    if escolha_sheldon == escolha_raj:
        return "De novo!"
    elif (
        (escolha_sheldon == "tesoura" and (escolha_raj == "papel" or escolha_raj == "lagarto"))
        or (escolha_sheldon == "papel" and (escolha_raj == "pedra" or escolha_raj == "Spock"))
        or (escolha_sheldon == "pedra" and (escolha_raj == "lagarto" or escolha_raj == "tesoura"))
        or (escolha_sheldon == "lagarto" and (escolha_raj == "Spock" or escolha_raj == "papel"))
        or (escolha_sheldon == "Spock" and (escolha_raj == "tesoura" or escolha_raj == "pedra"))
    ):
        return "Bazinga!"
    else:
        return "Raj trapaceou!"
        
# Função para ler a entrada e resolver o problema
def ler_entradas():
    casos_teste = int(input())  # Lê o número de casos de teste
    for i in range(1, casos_teste + 1):
        escolhas = input().split()  # Lê as escolhas de Sheldon e Raj para cada caso de teste
        escolha_sheldon = escolhas[0]
        escolha_raj = escolhas[1]
        resultado = verificar_reacao_sheldon(escolha_sheldon, escolha_raj)  # Verifica a reação de Sheldon
        print(f"Caso #{i}: {resultado}")  # Imprime a reação correspondente

# Chamada da função para ler a entrada e resolver o problema
ler_entradas()
