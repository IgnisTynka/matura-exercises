import random

def play(computer, player):
    match your_choice:
        case 'rock':
            if computer == 'paper':
                return 'Computer'
            elif computer == 'scissors':
                return 'You'
        case 'paper':
            if computer == 'scissors':
                return 'Computer'
            elif computer == 'rock':
                return 'You'
        case 'scissors':
            if computer == 'rock':
                return 'Computer'
            elif computer == 'paper':
                return 'You'
    return "Draw"

options = ['rock', 'paper', 'scissors']
computer_score = 0
your_score = 0

max_score = int(input("To how many points would you like to play? "))
while(max_score < 1):
    max_score = int(input("To how many points would you like to play? "))

while(your_score < max_score  and computer_score < max_score):
    computer_choice = random.choice(options)
    your_choice = input("Select rock, paper or scissors: ").lower()

    while(your_choice not in options):
        your_choice = input("Select rock, paper or scissors: ").lower()

    winner = play(computer_choice, your_choice)

    if(winner == "Computer"):
        print(f'Your choice: {your_choice}, computer choice: {computer_choice}\nComputer won')
        computer_score += 1
    elif(winner == "You"):
        print(f'Your choice: {your_choice}, computer choice: {computer_choice}\nYou won')
        your_score += 1
    else:
        print(f'Your choice: {your_choice}, computer choice: {computer_choice}\nDraw')

if(your_score == 3):
    print(f"\nCongrats! You won\nFinal score: You: {your_score}, Computer: {computer_score}")
else:
    print(f"\nThat's sad :c Computer won\nFinal score: You: {your_score}, Computer: {computer_score}")

