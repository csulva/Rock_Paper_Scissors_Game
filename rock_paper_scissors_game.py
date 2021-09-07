import random

# take in a number 0-2 from the user that represents their hand
user_hand = input('\nRock = 0\nPaper = 1\nScissors = 2\nChoose a number from 0-2: \n')

def get_hand(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'paper'
    elif number == 2:
        return 'scissors'
    else:
        print('Number must be between 0-2...')

def determine_winner(user, computer):
    if user == 'rock' and computer == 'paper':
        print(f'You chose {user} and the computer chose {computer}... the computer wins!')
    elif user == 'rock' and computer == 'scissors':
        print(f'You chose {user} and the computer chose {computer}... You win!')
    elif user == 'paper' and computer == 'scissors':
        print(f'You chose {user} and the computer chose {computer}... the computer wins!')
    elif user == 'paper' and computer == 'rock':
        print(f'You chose {user} and the computer chose {computer}... You win!')
    elif user == 'scissors' and computer == 'rock':
        print(f'You chose {user} and the computer chose {computer}... the computer wins!')
    elif user == 'scissors' and computer == 'paper':
        print(f'You chose {user} and the computer chose {computer}... You win!')
    elif user == computer:
        print(f'You chose {user} and the computer chose {computer}... It\'s a draw! Try again')

# call the function get_hand to get the string representation of the user's hand
user_choice = get_hand(int(user_hand))

# generate a random number 0-2 to use for the computer's hand
computer_hand = random.randint(0, 2)
# call the function get_hand to get the string representation of the computer's hand
computer_choice = get_hand(int(computer_hand))


# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner
determine_winner(user_choice, computer_choice)

while user_hand != 'exit'.lower():
    user_hand = input('Choose a number from 0-2: ')
    user_choice = get_hand(int(user_hand))
    computer_hand = random.randint(0, 2)
    computer_choice = get_hand(int(computer_hand))
    determine_winner(user_choice, computer_choice)





