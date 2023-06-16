def exibir_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(tabuleiro[i][j], end="|")
        print("\n---------")

def verificarvitoria(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True

    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def jogar():
    tabuleiro = [[" " for  in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        # Obter posição do jogador
        linha = int(input("Digite a linha (0, 1 ou 2): "))
        coluna = int(input("Digite a coluna (0, 1 ou 2): "))

        # Verificar se a posição está vazia
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Posição inválida. Tente novamente.")
            continue

        # Verificar se houve vitória
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print("Player", jogador_atual, "win!")
            break

        # Verificar se houve empate
        if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alternar jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

jogar()
