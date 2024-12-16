#Solve slot machine problem
#How much does user account have?
#What is the bet you are willing to place?
#user input number

import random

user_name = input('Hi, What is your name: ').title()
while True:
    game = input(f'Welcome {user_name}. If you want to continue, press "y" else press anything to quit! ').strip().lower()
    if game == 'y':
        break
    else:
        print("Input must be 'y' or 'n'")

print('What is your total amount and what will be your bet?')
user_amt = int(input('Total Amount: '))
user_bet = int(input('Your Bet: '))

def slot_Machine():
    inp1 = random.randint(1,4)
    inp2 = random.randint(1,4)
    inp3 = random.randint(1,4)
    return inp1,inp2,inp3

print(slot_Machine())

def slot_Steps():
    pass


while user_bet >= user_amt:
    pass