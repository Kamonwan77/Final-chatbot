bot_template = "BOT : {0}"

# Define variables
name = "Bot"
weather = "cloudy"

responses = {
    "what's your name?": "my name is {0}".format(name),
    "what's today's weather?": "the weather is {0}".format(weather),
    "default": "default message"
}

# Return the matching response if there is one, default otherwise
def respond(message):
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = responses["default"]
    return bot_message


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response
    print(bot_template.format(response))

# Send a message to the bot
print(bot_template.format("Hi!"))
value = input("USER : ")
send_message(value)
