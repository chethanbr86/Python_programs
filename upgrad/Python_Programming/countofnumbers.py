n = list(map(int,input()))

cnt_odd = 0
cnt_even = 0
cnt_zero = 0

for i in n:
    if i >= 0:
        if i%2==0 and i!=0:
            cnt_even = cnt_even + 1
        if i%2==1:
            cnt_odd = cnt_odd + 1
        if i == 0:
            cnt_zero = cnt_zero + 1
    else:
        print('Enter 0 or positive number')
        
print(f'The count of even numbers: {cnt_even}')
print(f'The count of odd numbers: {cnt_odd}')
print(f'The count of zeroes: {cnt_zero}')  



