# Goal
#
# I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it
# gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
#
# Allow the user to enter their question
# Display an in progress message( i.e. "thinking")
# Create 20 responses, and show a random response
# Allow the user to ask another question or quit
#
# Bonus Using whatever module you like, add a gui. Your gui must have:
#
# A box for users to enter the question
# At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

# From https://www.reddit.com/r/beginnerprojects/comments/29aqox/project_magic_8_ball/

# Use a dictionary and random numbers to select a response to the question.
from time import sleep
from random import randint

# Create dictionary to hold the responses.
responses = {1: "It is certain",
             2: "It is decidedly so",
             3: "Without a doubt",
             4: "Yes - definitely",
             5: "You may rely on it",
             6: "As I see it, yes",
             7: "Most likely",
             8: "Outlook good",
             9: "Yes",
             10: "Signs point to yes",
             11: "Reply hazy, try again",
             12: "Ask again later",
             13: "Better not tell you now",
             14: "Cannot predict now",
             15: "Concentrate and ask again",
             16: "Don't count on it",
             17: "My reply is 'No'",
             18: "My sources say no",
             19: "Outlook not so good",
             20: "Very doubtful"}

question = input("Please enter your question for the Magic 8 Ball, or quit: ")
while True:
    if question.lower() == 'quit':
        break
    else:
        print("Well...an intriguing query...please, let me consult the spirits...")
        print()
        # Add dramatic pause for drama.
        sleep(2)

        print("After consultation, my response is:", responses[randint(1, 21)])
        print()
        question = input("Please enter your next question, or quit: ")

# Add GUI to program.