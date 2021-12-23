#To convert string input to int
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))
print(len(two_digit_number))

def dig_split(n):
    if len(n) != 2:
        print('Please print 2 digit number')
    return list(map(int,str(n)))

print(dig_split(two_digit_number))

print(sum(dig_split(two_digit_number)))