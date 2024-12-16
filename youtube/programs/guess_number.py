import random
# play = input('wanna play, press y? ').lower().strip()
# if play != 'y':
#     quit()

# Note: computer_gen = random.randrange(11) # 11 not included and starts from 0, also randint(0,11) (11 included) can be used but have to give 2 arguments
# user_input = int(input('Guess a number between 0 to 10: '))

#Type1: using quit()
# user_input = input('Guess a number between 0 to 10: ')

# if user_input.isdigit():
#     user_input = int(user_input)
#     if user_input > 10 or user_input < 0:
#         print('Should be between 0 and 10 both included!')
#         quit()
# else:
#     print('only digits allowed')
#     quit()
# print(f'User input: {user_input}')
# computer_gen = random.randrange(0,user_input)
# print(f'Computer input: {computer_gen}')

#Type2: using while loop with continue and break
# while True: #another way
#     try:
#         user_input = int(input("Enter a number: "))
#         break  # Exit the loop if input is valid
#     except ValueError:
#         print("Error: That's not a valid number. Please enter an integer.")
guesses = 0
while True:
    guesses += 1
    user_input = input("Enter a number between 0 and 10: ")

    if user_input.isdigit():        
        user_input = int(user_input)
        if user_input > -1 and user_input <= 10:
            print("Let's Play!")
        else:
            print('should be between 0 and 10')
            continue
    else:
        print('only digits allowed')
        continue

    computer_gen = random.randrange(0,11) #the range 11 can be replaced with user_input if you want to go in a direction of computer generated number
    print(f'Computer input: {computer_gen}')

    if user_input == computer_gen:
        print(f"user_input: {user_input} and computer_gen: {computer_gen} are matching.")
        break
    elif user_input > computer_gen:
        print(f"user_input: {user_input} was greater than computer_gen: {computer_gen}!")
    else:
        print(f"user_input: {user_input} was lesser than computer_gen: {computer_gen}!")

print(f'You made {guesses} guesses!')