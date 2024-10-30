bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = ["tell me more!", "why do you think that?"]

import random
def respond(message):
    if message in responses:
        return random.choice(responses)
respond("I think you're really great")


def send_message():
    while True:

        message = input("USER: ")

        if message.lower() == 'bye':
            print("BOT: Goodbye!")
            break

        response = respond(message)

        print(bot_template.format(response))


send_message()
