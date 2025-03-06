def findMissingAndRepeatedValues(grid):    
    for i in range(len(grid)-1):
        List = [item for sublist in grid for item in sublist]
    print(List)

    rep_miss = []

    for i in range(1,len(List)):
        if List[i] == List[i-1]:
            rep_miss.append(List[i])
        if List[i]-List[i-1] > 1 or List[i]-List[i-1] < 0:
            rep_miss.append(int((List[i]+List[i-1])/2))
    return rep_miss        

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
    print(findMissingAndRepeatedValues(grid))

#In leetcode, the below part is not required to be pasted, but in codechef, we need to