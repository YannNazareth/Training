from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot ('Steve')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.portuguese")

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response("how are you")
    if float(resposta.confidence) < 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')