#To convert string input to int
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
#myway
# print(type(two_digit_number))
# print(len(two_digit_number))

# def dig_split(n):
#     if len(n) != 2:
#         return 0
#     return list(map(int,str(n)))

# if 0:
#     print('Please print 2 digit number')
# else:
#     print(dig_split(two_digit_number))
#     print(sum(dig_split(two_digit_number)))

    #fix this

#udemy way

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(int(first_digit)+int(second_digit))