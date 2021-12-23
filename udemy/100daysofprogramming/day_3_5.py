print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
S = 15
M = 20
L = 25
ps = 2
pa = 3
e = 1

if size == 'S':
    bill = S
    if add_pepperoni == 'Y':
        bill = S+ps
    if extra_cheese == 'Y':
        bill = S+ps+e            
    else:
        print(f'Your total bill is: {S}')