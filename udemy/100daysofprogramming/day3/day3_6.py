print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
# S = 15
# M = 20
# L = 25
# ps = 2
# pa = 3
# e = 1

#udemy
if size == 'S':
    bill += 15  
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2 
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1           

print(f'Your total bill is: {bill}')