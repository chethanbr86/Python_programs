#if number divisible by 3 fizz, if by 5 buzz, if by both then fizzbuzz

for i in range(1,101):
    if i%3 == 0:
        print('Fizz')         
    elif i%5 == 0:
        print('Buzz')
    elif i%3 == 0 and i%5 == 0:
        print('FizzBuzz')
    # elif i%3 != 0 and i%5 != 0:
    else:
        print(i)

#lesson
# for i in range(1,101):
#     if i%3 == 0:
#         print('Fizz')         
#     if i%5 == 0:
#         print('Buzz')
#     if i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)
#This is where the difference between elif and if can be found

#udemy
#Better coding way
# for i in range(1,101):
#     if i%3 == 0 and i%5 == 0:
#         print('FizzBuzz')         
#     elif i%5 == 0:
#         print('Buzz')
#     elif i%3 == 0:
#         print('Fizz')
#     else:
#         print(i)