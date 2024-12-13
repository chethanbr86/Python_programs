# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#         break  # Exit the loop if input is valid
#     except ValueError:
#         print("Error: That's not a valid number. Please enter an integer.")

# print(f"You entered the number: {user_input}")

# user_input = input()

# database1 = ''
# database1 = database1 + user_input
# print(user_input,database1)

# database2 = []
# database2.append(user_input)
# print(user_input,database2[-1])

import random
def Slot_Machine():
    inp1 = random.randint(1,3)
    inp2 = random.randint(1,3)
    inp3 = random.randint(1,3)
    return inp1,inp2,inp3

print(Slot_Machine())


    