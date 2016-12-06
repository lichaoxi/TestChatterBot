from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ron Obvious")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "谢谢",
    "不用谢"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
response = chatbot.get_response("谢谢")
print(response)