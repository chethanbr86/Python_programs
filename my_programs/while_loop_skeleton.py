# Type - 1
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     while True:
#         List1 = list(map(int, input().split()))
#         List2 = list(map(int, input().split()))
        
#         if len(List1) != n or len(List2) != n:
#             print('Error: Length of lists does not match n')
#             continue
#         break
#     grid = [List1, List2]
#     print(grid)

# Type - 2
# t = int(input())
# while t:     
#     t -= 1    
#     no_of_person, money_units = list(map(int,input().split()))
#     withdraw = list(map(int,input().split()))    
#     if len(withdraw) != no_of_person:
#         print('wrong entry')
#         continue
#     else:
#         for j in withdraw: 
#             if j <= money_units:
#                 money_units -= j
#                 print(1, end='')
#             else:
#                 print(0, end='')
#     print('\n')
