t = int(input())
for _ in range(t):
    n = int(input())
    while True:
        List1 = list(map(int, input().split()))
        List2 = list(map(int, input().split()))
        
        if len(List1) != n or len(List2) != n:
            print('Error: Length of lists does not match n')
            continue
        break
    grid = [List1, List2]
    print(grid)
