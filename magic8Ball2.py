import random

messages = [
    "It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]

# This line chooses a number between 0 and the length of the list
# This means you can change the list without changing the below code.
print(messages[random.randint(0, len(messages) - 1)])
