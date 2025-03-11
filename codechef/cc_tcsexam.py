def Winner(d,s):
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