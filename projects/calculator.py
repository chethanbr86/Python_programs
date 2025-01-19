class calculator:

    def f_add(num1, num2):
        return num1 + num2
    
    def f_sub(num1, num2):
        return num1 - num2
    
    def f_mul(num1, num2):
        return num1 * num2
    
    def f_div(num1, num2):
        if num2 == 0:
            print('Number not divisible by 0')
        return num1 // num2
    
# print(calculator.f_add(15,6))
# print(calculator.f_sub(15,6))
# print(calculator.f_mul(15,6))
# print(calculator.f_div(16,6))

# user_input = int(input())
# for i in range(user_input):
#     n = list(map(int, input().split()))
#     num1 = n[0]
#     num2 = n[1]

while True:
    user_inp = input('Enter 2 numbers or press q to exit: ')
    if user_inp != 'q':
        num1 = int(input())
        num2 = int(input()) #need to do loop for digit and alphabet validation
    
        user_input = input('If you want to add press a, to substract press s, to multiply press m, to divide press d, to exit press e: ')
        if user_input == 'e':
            break
        if user_input == 'a':
            print(calculator.f_add(num1, num2))
        elif user_input == 's':
            print(calculator.f_sub(num1, num2))
        elif user_input == 'm':
            print(calculator.f_mul(num1, num2))
        elif user_input == 'd':
            print(calculator.f_div(num1, num2))
        else:
            print('Invalid')
            continue
    else:
        break