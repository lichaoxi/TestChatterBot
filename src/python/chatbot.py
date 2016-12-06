from chatterbot import ChatBot

bot = ChatBot(
    "Norman",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    database="./database.json"
)

while True:
    try:
        bot_input = bot.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break