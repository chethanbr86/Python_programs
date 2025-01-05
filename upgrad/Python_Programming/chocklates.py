'''Sanjay sees than, upon bringing 3 wrappers of the same chocolate, 
you will get new chocolate for free. If Sanjay has m Rupees. 
How many chocolates will he be able to eat if each chocolate costs c Rupees?'''

# 1st way:
m = int(input()) #No of rupees Sanjay has
c = int(input()) #Cost of each chocklate

# Taking 2 inputs at once
x = input()
my_list = x.split(' ') #give 2 inputs with space

m = int(my_list[0])
c = int(my_list[1])

choc = m//c #No of chocklates Sanjay can eat
w = choc #Wrappers left with Sanjay which he can exchange

while w//3 != 0: #Until chocklate wrappers left is not equal to zero, (see if w//3 < 3 applies too)
    choc = choc + w//3 #Total number of chocklates first purchased and then exchanged with wrappers
    w = w//3 + w%3
print(f'Total number of chocklates Sanjay can eat: {choc}')