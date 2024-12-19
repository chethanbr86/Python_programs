#Solve slot machine problem
#How much does user account have?
#What is the bet you are willing to place?
#user input number

import random

#myway - not complete
# user_name = input('Hi, What is your name: ').title()
# while True:
#     game = input(f'Welcome {user_name}. If you want to continue, press "y" else press anything to quit! ').strip().lower()
#     if game == 'y':
#         break
#     else:
#         print("Input must be 'y' or 'n'")

# print('What is your total amount and what will be your bet?')
# user_amt = int(input('Total Amount: '))
# user_bet = int(input('Your Bet: '))

# def slot_Machine():
#     inp1 = random.randint(1,4)
#     inp2 = random.randint(1,4)
#     inp3 = random.randint(1,4)
#     return inp1,inp2,inp3

# print(slot_Machine())

# def slot_Steps():
#     pass

# while user_bet >= user_amt:
#     pass

MIN_LINES = 1 #for mine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
min1 = 1 #for mine
max1 = 100 #for mine
ROWS = 3
COLS = 3

#Note - these 3 functions can be written in a single function but can be used with separate variables
#mostly like
# def placeholder(min1,max1,txt=''):
#     while True:
#         amount = input(f'What would you like to deposit?{txt}: ${min1} - ${max1}? $') #See how to write dynamic input text
#         if amount.isdigit():
#             amount = int(amount)
#             if min1 <= amount <= max1:
#                 break
#             else:
#                 print(f'Amount must be between ${min1} - ${max1}')
#         else:
#             print('Please enter a positive number')
#     return amount

# def main():
#     balance = placeholder(MIN_BET,MAX_BET,'What will be your deposit? ')
#     lines = placeholder(MIN_LINES,MAX_LINES, 'How many lines? ')
#     while True:
#         bet = placeholder(MIN_BET,MAX_BET,'What is the bet amount? ') #I would not have thought about putting this line under while loop
#         total_bet = bet * lines
#         if total_bet > balance:
#             print(f'You do not have enough to bet that amount, your current balance is ${balance} and you are betting ${total_bet}')
#         else:
#             break
#     print(f'You are betting ${bet} on {lines} lines for a total bet of ${total_bet} with a deposit of {balance}')

#youtubeway
def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Please enter a positive number')
    return amount

def get_number_of_lines():
    while True:
        # lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(f'Lines must be between 1 and {MAX_LINES}')
        else:
            print('Please enter a positive number')
    return lines

def get_bet():
    while True:
        amount = input(f'What would you like to bet on each line between ${MIN_BET} - ${MAX_BET}? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Please enter a positive number')
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet() #I would not have thought about putting this line under while loop
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is ${balance} and you are betting ${total_bet}')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines for a total bet of ${total_bet} with a deposit of {balance}')

main()