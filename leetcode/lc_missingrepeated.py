#myway expect for sublist = list(map(int, input().split())) - accepted
def findMissingAndRepeatedValues(grid):        
    for i in range(len(grid)-1):
        List = [item for sublist in grid for item in sublist]
        List.sort()
    print(List)

    rep_miss1 = []
    rep_miss2 = []
    def repeat():
        for i in range(1,len(List)):
            if List[i] == List[i-1]:
                rep_miss1.append(List[i])
        return rep_miss1

    def missing():
        for i in range(1,len(List)):
            if List[i]-List[i-1] > 1 or List[i]-List[i-1] < 0:
                rep_miss2.append(int((List[i]+List[i-1])/2))
        if len(rep_miss2) == 0:
            if List[0]-1 != 0:
                rep_miss2.append(List[0]-1)
            else:
                rep_miss2.append(List[i]+1)
        return rep_miss2
    
    rep_miss_list = [repeat(),missing()]
    final_List = [item for sublist in rep_miss_list for item in sublist]

    return final_List

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     grid = []
#     while len(grid) != n:
#         # List1 = list(map(int, input().split()))
#         # List2 = list(map(int, input().split()))
        
#     #     if len(List1) != n or len(List2) != n:
#     #         print('Error: Length of lists does not match n')
#     #         continue
#     #     break
#     # grid = [List1, List2]
#         grid.append(list(map(int, input().split())))
#     print(findMissingAndRepeatedValues(grid))

t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    while len(grid) != n:
        sublist = list(map(int, input().split()))
        if len(sublist) != n:
            print('Error: Length of sublist does not match n')
            continue
        grid.append(sublist)
    print(findMissingAndRepeatedValues(grid))

# The final output is getting sorted too, make 2 different functions