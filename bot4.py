
bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = { "what's your name?": [
    "my name is EchoBot",
    "they call me EchoBot",
    "the name's Bot, EchoBot"
    ]
}


import random
def respond(message):

    if message in responses:
        return random.choice(responses[message])

respond("what's your name?")


def send_message():
    while True:

        message = input("USER: ")

        if message.lower() == 'bye':
            print("BOT: Goodbye!")
            break

        response = respond(message)

        print(bot_template.format(response))


send_message()
