
bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = { "what's today's weather?": "it's {} today"}


weather_today = "cloudy"

def respond(message):

    if message in responses:

        return responses[message].format(weather_today)

respond("what's today's weather?")


def send_message():
    while True:

        message = input("USER: ")

        if message.lower() == 'bye':
            print("BOT: Goodbye!")
            break

        response = respond(message)

        print(bot_template.format(response))


send_message()