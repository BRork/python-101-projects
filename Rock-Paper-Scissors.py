import random


def jankenpon():
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("Your options are: ")
        throw = ['Rock', 'Paper', 'Scissors']
        c_throw = ['Rock', 'Paper', 'Scissors']
        for option in throw:
            print(option)
        while True:
            choice = str(input('Enter your selection: '))
            if choice.lower() == 'rock' or choice.lower() == 'paper' or choice.lower() == 'scissors':
                break
            else:
                print('This is an invalid input, please enter Rock, Paper, or Scissors')
                continue   
        c_choice = random.choice(c_throw)
        print('Computer throws: ' + c_choice)
        if c_choice.lower() == choice.lower():
            print('Result: Tie')
        elif c_choice.lower() == 'rock' and choice.lower() == 'scissors' or c_choice.lower() == 'paper' and choice.lower() == 'rock' or c_choice.lower() == 'scissors' and choice.lower() == 'paper':
            print("Result: Computer Wins")
        else:
            print('Result: Player Wins')
        rept = str(input('Do you want to play again? Y/N: '))
        if rept.upper() == 'Y':
            continue
        else:
            break
            
            
jankenpon()