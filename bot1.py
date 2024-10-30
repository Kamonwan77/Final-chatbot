

bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = {"what's your name?": "my name is EchoBot",
            "what's the weather today?": "it's sunny!"}


def respond(message):
    if message in responses:
        return responses[message]

respond("what's your name?")


def respond(message):
    bot_message = "I can hear you! you said: " + message

    return bot_message


def send_message():
    while True:

        message = input("USER: ")

        if message.lower() == 'bye':
            print("BOT: Goodbye!")
            break

        response = respond(message)

        print(bot_template.format(response))


send_message()

