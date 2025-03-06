def findMissingAndRepeatedValues(grid):    
    for i in range(len(grid)-1):
        List = [item for sublist in grid for item in sublist]
    print(List)

    for i,j in List:
        print(i,j)

    repeated = []
    missing = []
    

#In leetcode, the below part is not required to be pasted, but in codechef, we need to
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
    findMissingAndRepeatedValues(grid)
