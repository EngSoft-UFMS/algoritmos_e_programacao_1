# Função para retornar as perguntas

def retornar_perguntas():
    perguntas = [
        {
            'pergunta': 'Qual é a capital da França?',
            'opcoes': ['Paris', 'Londres', 'Roma', 'Madri'],
            'resposta': 'Paris'
        },
        {
            'pergunta': 'Qual é o maior planeta do Sistema Solar?',
            'opcoes': ['Júpiter', 'Vênus', 'Saturno', 'Marte'],
            'resposta': 'Júpiter'
        },
        {
            'pergunta': 'Quem pintou a Mona Lisa?',
            'opcoes': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],
            'resposta': 'Leonardo da Vinci'
        },
        {
            'pergunta': 'Qual é o rio mais longo do mundo?',
            'opcoes': ['Rio Amazonas', 'Rio Nilo', 'Rio Mississippi', 'Rio Yangtzé'],
            'resposta': 'Rio Nilo'
        },
        {
            'pergunta': 'Qual é a capital do Canadá?',
            'opcoes': ['Ottawa', 'Toronto', 'Montreal', 'Vancouver'],
            'resposta': 'Ottawa'
        }
        {
            'pergunta': 'Qual é a capital do Mato Grosso do Sul?',
            'opcoes': ['Campo Grande', 'São Paulo', 'Rio de Janeiro', 'Três Lagos'],
            'resposta': 'Campo Grande'
        }
        {
            'pergunta': 'Qual é a capital do Brasil?',
            'opcoes': ['Rio de Janeiro', 'Salvador', 'São Paulo', 'Brasília'],
            'resposta': 'Brasília'
        }
    ]
    return perguntas
 
# Função para mostrar as opções de resposta e retornar a resposta do usuário

def fazer_pergunta(pergunta):
    print(pergunta['pergunta'])
    for i, opcao in enumerate(pergunta['opcoes']):
        print(f'{i+1}. {opcao}')

    resposta = input('Digite o número da opção correta: ')
    return resposta

# Função para verificar se a resposta do usuário é correta
def menu()-> int:
    print("Bem-Vindo ao jogo de Perguntas e respostas")
    print("Escolha um modo de jogo:")
    print("1- Fácil")
    print("2- Médio")
    print("3- Difícil")
    numero = int(input())
    return numero

def verificar_resposta(pergunta, resposta):
    return pergunta['opcoes'][int(resposta) - 1] == pergunta['resposta']

# Função que contém as perguntas e inicia o jogo

def jogar():
    perguntas = carregar_perguntas()
    pontos = 0

    print('Bem-vindo ao jogo de perguntas e respostas!')
    print('Responda corretamente o maior número de perguntas para ganhar pontos.')

menu()

