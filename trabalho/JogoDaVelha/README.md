Trabalho: Jogo da Velha em Python

Neste trabalho, você irá implementar o jogo da velha em Python. O jogo será desenvolvido por meio de funções e seguirá as regras tradicionais do jogo. O programa permitirá que dois jogadores participem alternadamente, exibindo o tabuleiro a cada jogada e verificando se houve vitória ou empate.

Siga as instruções abaixo para desenvolver o programa:

Crie uma função chamada exibir_tabuleiro(tabuleiro) que recebe como parâmetro uma lista tabuleiro representando o estado atual do jogo. Essa função será responsável por exibir o tabuleiro na tela, mostrando as marcações dos jogadores e as linhas e colunas. Utilize caracteres para desenhar as linhas horizontais e verticais, como no exemplo abaixo:
![image](https://github.com/EngSoft-UFMS/algoritmos_e_programacao_1/assets/127705012/82a6a338-e234-4626-a0e8-c598fd83ca13)
Crie uma função chamada verificar_vitoria(tabuleiro, jogador) que recebe como parâmetro uma lista tabuleiro representando o estado atual do jogo e uma string jogador representando o jogador atual ("X" ou "O"). Essa função será responsável por verificar se o jogador atual venceu o jogo. Utilize a lógica de verificação de vitória do jogo da velha, verificando as linhas, colunas e diagonais.

Crie uma função chamada jogar() que irá conter a lógica principal do jogo. Dentro dessa função, inicialize o tabuleiro como uma lista de listas, onde cada posição é inicializada com o caractere espaço em branco (" "). Defina também a variável jogador_atual como a string "X", indicando que o jogador X será o primeiro a jogar.

Dentro da função jogar(), utilize um loop while True para repetir o jogo até que haja um vencedor ou empate. A cada iteração do loop, exiba o tabuleiro chamando a função exibir_tabuleiro(tabuleiro).

Solicite ao jogador a posição que ele deseja marcar. Peça ao jogador para digitar a linha e a coluna onde deseja fazer a jogada. Utilize as funções input() e int() para obter as informações do jogador. Lembre-se de verificar se a posição escolhida está vazia no tabuleiro.

Se a posição escolhida estiver vazia, atualize o tabuleiro com a marca do jogador atual. Caso contrário, exiba uma mensagem de erro e peça ao jogador para escolher outra posição.

Após a jogada, chame a função verificar_vitoria(tabuleiro, jogador_atual) para verificar se o jogador atual venceu o jogo. Se a função retornar True, exiba o tabuleiro final chamando a função exibir_tabuleiro(tabuleiro) e anuncie o vencedor.

Verifique se houve empate no jogo. Para isso, verifique se todas as posições do tabuleiro estão preenchidas. Se todas estiverem preenchidas e ninguém venceu, exiba o tabuleiro final e anuncie o empate.
