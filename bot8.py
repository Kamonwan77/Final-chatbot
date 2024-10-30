import random

# Define possible responses for statements, questions, and default cases
responses = {
    'statement': [
        'Tell me more!',
        'Why do you think that?',
        'How long have you felt this way?',
        'I find that extremely interesting.',
        'Can you back that up?',
        'Oh wow!',
        ':)'
    ],
    'question': [
        "I don't know :(",
        'You tell me!'
    ],
    'default': [
        "I'm not sure I understand.",
        "Could you elaborate on that?"
    ]
}

# Templates for bot and user messages
bot_template = "BOT : {0}"
user_template = "USER : {0}"

def get_response(message):
    """
    Generates a response based on whether the message is a question or statement.
    """
    message = message.strip().lower()

    if message.endswith('?'):
        # If the message is a question, choose from 'question' responses
        response = random.choice(responses.get("question", responses["default"]))
    elif message:
        # If the message is a statement, choose from 'statement' responses
        response = random.choice(responses.get("statement", responses["default"]))
    else:
        # If the message is empty, prompt the user
        response = "Please say something so I can respond."

    return response

def send_message():
    """
    Handles the chat loop, taking user input and responding accordingly.
    """
    print(bot_template.format("Hello! I'm ChatBot. How can I assist you today?"))

    while True:
        user_input = input(user_template.format(""))

        if user_input.lower() == "bye":
            print(bot_template.format("Goodbye! Have a great day!"))
            break

        response = get_response(user_input)
        print(bot_template.format(response))

# Start the chatbot
send_message()
