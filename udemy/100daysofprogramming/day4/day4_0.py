import random
def rps(num):
    
    rock = ''' 
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = ''' 
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = ''' 
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    if num == 0:
        return f'Rock {rock}'
    if num == 1:
        return f'Paper {paper}'
    if num == 2:
        return f'Scissors {scissors}'
# scissors cuts paper, paper covers rock, and rocks crushes scissors
# Rock wins against sciccors, scissors win against paper, paper wins against rock
# outcomes: won, lost, draw
#Write your code below this line 👇

# user_inp = int(input('Enter 0, 1 or 2: ', ))
# print(f'user chose: {user_inp}')
# comp_inp = random.randint(0,2)
# print(f'computer chose {comp_inp}')

# if user_inp == comp_inp:
#     print('Draw')

# if user_inp == 0 and comp_inp == 1:
#     print(f'{rps(comp_inp)} beats {rps(user_inp)}')
# if user_inp == 0 and comp_inp == 2:
#     print(f'{rps(user_inp)} beats {rps(comp_inp)}')
# if user_inp == 1 and comp_inp == 0:
#     print(f'{rps(user_inp)} beats {rps(comp_inp)}')
# if user_inp == 1 and comp_inp == 2:
#     print(f'{rps(comp_inp)} beats {rps(user_inp)}')
# if user_inp == 2 and comp_inp == 0:
#     print(f'{rps(comp_inp)} beats {rps(user_inp)}')
# if user_inp == 2 and comp_inp == 1:
#     print(f'{rps(user_inp)} beats {rps(comp_inp)}')

#Another solution
user_wins = 0
computer_wins = 0

# options = ['rock','paper','scissor']
options = ['r','p','s']

while True:
    user_input = input('Enter r, p or s or "q": ', ).lower()
    if user_input == 'q':
        break 
    if user_input not in options:
        continue

    print(f'User_input: {user_input}')
    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print(f'Computr_input: {computer_input}')

    if user_input == 'r' and computer_input == 's':
        print(f'User wins')
        user_wins += 1        
    elif user_input == 'p' and computer_input == 'r':
        print(f'User wins')
        user_wins += 1        
    elif user_input == 's' and computer_input == 'p':
        print(f'User wins')
        user_wins += 1
    else:
        print('Computer wins')
        computer_wins += 1

print(f'User wins: {user_wins} times.')
print(f'Computer wins: {computer_wins} times.')
print('Thanks for playing')

#udemy solution

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")
