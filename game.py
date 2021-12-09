# contact : wasif.hossain27@gmail.com
# Rock paper Scissor Game
import random

lst = ['Rock', 'Paper', 'Scissor']
print(f"""
Welcome To Rock , Paper , Scissor Game
You have 5 chances to prove yourself
Follow the instruction
enter r for Rock
enter p for paper
enter s for scissor
-----------------------------------
""")

total = 0
i = 1
while i < 6:

    user = input(f"\n{i}.Choose your Choice >>> ")

    bot_choice = random.choice(lst)
    bot_choice2 = bot_choice[0].lower()

    if user == bot_choice2:
        print(">>> YOU WON :)  the bot picked - ", bot_choice)
        total += 1
    elif user != bot_choice2:
        print(">>> *** YOU LOSE :(  the bot picked - ", bot_choice)
    else:
        print('Invalid Input')

    i += 1

print(f"\n\nYour Score is --> {total}\nThank you for playing this game\n>>>>> Wasif Hossain  :)")
