import random

bot_template = "BOT : {0}"

# Define variables
name = "Bot"
weather = "cloudy"

responses = {
    "what's your name?": [
        "my name is {0}".format(name),
        "they call me {0}".format(name),
        "I am {0}".format(name)
    ],

    "what's today's weather?": [
        "the weather is {0}".format(weather),
        "it's {0} today".format(weather)
    ],
    "default": ["default message"]
}

# Return the matching response if there is one, default otherwise
def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message():
    while True:

        message = input("USER: ")

        if message.lower() == 'bye':
            print("BOT: Goodbye!")
            break

        response = respond(message)

        print(bot_template.format(response))


send_message()
# Send a message to the bot
print(bot_template.format("Hi!"))
value = input("USER : ")
send_message(value)
