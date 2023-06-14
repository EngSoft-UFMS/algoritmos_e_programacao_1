# Função para retornar as perguntas

def retornar_perguntas():
    perguntas = [
        {
            'pergunta': 'Qual é a capital da França?',
            'opcoes': ['Paris', 'Londres', 'Roma', 'Madri'],
            'resposta': 'Paris'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Qual é o maior planeta do Sistema Solar?',
            'opcoes': ['Júpiter', 'Vênus', 'Saturno', 'Marte'],
            'resposta': 'Júpiter'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Quem pintou a Mona Lisa?',
            'opcoes': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh', 'Michelangelo'],
            'resposta': 'Leonardo da Vinci'
            'categoria' : 'Artes'
        },
        {
            'pergunta': 'Qual é o rio mais longo do mundo?',
            'opcoes': ['Rio Amazonas', 'Rio Nilo', 'Rio Mississippi', 'Rio Yangtzé'],
            'resposta': 'Rio Nilo'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Qual é a capital do Canadá?',
            'opcoes': ['Ottawa', 'Toronto', 'Montreal', 'Vancouver'],
            'resposta': 'Ottawa'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Qual é a capital do Mato Grosso do Sul?',
            'opcoes': ['Campo Grande', 'São Paulo', 'Rio de Janeiro', 'Três Lagos'],
            'resposta': 'Campo Grande'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Qual é a capital do Brasil?',
            'opcoes': ['Rio de Janeiro', 'Salvador', 'São Paulo', 'Brasília'],
            'resposta': 'Brasília'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Qual é a capital de São Paulo?',
            'opcoes': ['Rio de Janeiro', 'Salvador', 'São Paulo', 'Brasília'],
            'resposta': 'São Paulo'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Qual é a maior montanha do mundo?',
            'opcoes': ['Monte Everest', 'K2', 'Makalu', 'Cho Oyu'],
            'resposta': 'Monte Everest'
            'categoria' : 'Geografia'
        },
        {
            'pergunta': 'Quem é o autor de Abaporu?',
            'opcoes': ['Tarsila do Amaral', 'Candido Portinari', 'Anita Malfatti', 'Vicente do Rego'],
            'resposta': 'Tarsila do Amaral'
            'categoria' : 'Artes'
        },
        {
            'pergunta': 'Quem pintou a obra A Criação de Adão?',
            'opcoes': ['Michelangelo Buonarotti', 'Leonardo Da Vinci', 'Pablo Picasso', 'Edvard Munch'],
            'resposta': 'Michelangelo Buonarotti'
            'categoria' : 'Artes'
        },
        {
            'pergunta': 'Qual artista considerado o pai do Cubismo?',
            'opcoes': ['Pablo Picasso', 'Vincent van Gogh', 'Tarsila do Amaral', 'Vicente do Rego Monteiro'],
            'resposta': 'Pablo Picasso'
            'categoria' : 'Artes'
        }
    ]
    return perguntas
 
# Função para mostrar as opções de resposta e retornar a resposta do usuário
def categoria()-> int:
    print("Escolha a categoria que você deseja responder:")
    print("1- Geografia")
    print("2- Artes")
    print("3- História")
    print("4- Ciência")
    print("5- Esportes")
    print("6- Entretenimento")
    print("7- Sair")
    opcao = int(input())
    return opcao

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
    print("4- Sair")
    numero = int(input())
    return numero

def verificar_resposta(pergunta, resposta):
    return pergunta['opcoes'][int(resposta) - 1] == pergunta['resposta']

# Função que contém as perguntas e inicia o jogo

def jogar():
    cont = menu()

    if cont == 1:
        pass

    elif cont == 2:
        pass

    elif cont == 3:
        pass

    elif cont == 4:
        pass
    

    perguntas = retornar_perguntas()
    pontos = 0

    print('Bem-vindo ao jogo de perguntas e respostas!')
    print('Responda corretamente o maior número de perguntas para ganhar pontos.')

    for pergunta in perguntas:
        resposta = fazer_pergunta(pergunta)
        if verificar_resposta(pergunta, resposta):
            pontos += 1
            print('Resposta correta!\n')
        else:
            print(f'Resposta incorreta! A resposta correta era: {pergunta["resposta"]}\n')

    print(f'Fim de jogo! Você marcou {pontos} pontos de um total de {len(perguntas)}.')
    

jogar()
