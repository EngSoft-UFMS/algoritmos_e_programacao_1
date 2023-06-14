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

def verificar_resposta(pergunta, resposta):
    return pergunta['opcoes'][int(resposta) - 1] == pergunta['resposta']

