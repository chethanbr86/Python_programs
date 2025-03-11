def Winner(d,s):
    total_d = 0
    total_s = 0
    for i in d:
        total_d = total_d + i
    for j in s:
        total_s = total_s + j

    if total_d != total_s:
        if total_d > total_s:
            print('Dragon')
        else:
            print('Sloth')

    else:
        pass

    


t = int(input())
for _ in range(t):
    while True:
        dragon = list(map(int, input().split()))
        if len(dragon) == 3:
            break
        print('Error: Length of dragon list does not match 3. Please enter again.')

    while True:
        sloth = list(map(int, input().split()))
        if len(sloth) == 3:
            break
        print('Error: Length of sloth list does not match 3. Please enter again.')

    Winner(dragon,sloth)