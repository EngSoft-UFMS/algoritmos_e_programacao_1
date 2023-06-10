# Jogo do Nim

def computador_escolhe_jogada(n, m):
    jogada = 1
    while jogada <= m:
        if (n - jogada) % (m + 1) == 0:
            return jogada
        jogada += 1
    return m

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada < 1 or jogada > m or jogada > n:
        print("Jogada inválida. Tente novamente.")
        jogada = int(input("Quantas peças você vai tirar? "))
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Computador começa!")
        vez_do_computador = True
    else:
        print("Você começa!")
        vez_do_computador = False

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            print("\nO computador tirou", jogada, "peça(s).")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            print("\nVocê tirou", jogada, "peça(s).")

        n -= jogada
        print("Agora resta(m)", n, "peça(s) no tabuleiro.\n")

    if vez_do_computador:
        print("Fim do jogo! O computador ganhou!")
        return 0
    else:
        print("Fim do jogo! Você ganhou!")
        return 1

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, 4):
        print("\n**** Rodada", rodada, "****\n")
        resultado = partida()

        if resultado == 1:
            placar_usuario += 1
        else:
            placar_computador += 1

    print("\n*** Final do campeonato! ***\n")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato\n")

opcao = int(input("Sua opção: "))

if opcao == 1:
    print("\nVocê escolheu uma partida isolada!\n")
    partida()
elif opcao == 2:
    print("\nVocê escolheu um campeonato!\n")
    campeonato()
else:
    print("Opção inválida.")
