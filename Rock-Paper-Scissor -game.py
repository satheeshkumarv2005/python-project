import random

user_choice = input('enter your choice(rock/paper/scissor)')
print(f'user choosed as {user_choice}')
computer_choice = random.choice(['rock','paper','scissor'])
print(f'computer choosed as {computer_choice}')

if user_choice == computer_choice:
    print('game tied')
else:
    if user_choice == 'scissor':
        if computer_choice == 'paper':
            print('user won the game')
        else:
            print('computer won the game')

    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print('user won the game')
        else:
            print('computer won the game')

    elif user_choice == 'rock':
        if computer_choice == 'scissor':
            print('user won the game')
        else:
            print('computer won the game')

    else:
        print('invalid choice.enter the proper choice to continue the game')
