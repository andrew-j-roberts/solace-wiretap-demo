from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def get_english_chatbot():
    chatbot = ChatBot('Mr. Robot')
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

    return chatbot