import random

# Definindo as respostas padrão
respostas_padrao = [
    "Olá, meu nome é Colombo. Como posso ajudá-lo?",
    "Eu sou Colombo, como posso ser útil?",
    "Olá, sou a inteligência artificial Colombo. Em que posso ajudá-lo?",
    "Bem-vindo! Eu sou Colombo, o que você precisa?"
    # Adicione aqui mais respostas padrão
]

# Definindo a função de resposta do chatbot
def responder_mensagem(mensagem):
    # Verificando se a mensagem contém uma saudação
    if "olá" in mensagem.lower() or "oi" in mensagem.lower() or "olá, colombo" in mensagem.lower():
        return random.choice(respostas_padrao)
    # Adicione aqui outras condições de resposta, de acordo com o que o chatbot deve responder

# Loop principal do chatbot
while True:
    mensagem = input("Você: ")
    resposta = responder_mensagem(mensagem)
    print("Colombo: " + resposta)
