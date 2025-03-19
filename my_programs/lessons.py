'''
input can be taken in 2 ways:
1st with while loop 
2nd with for and while loop
'''
# t = int(input())
# while t:     
#     t -= 1    
#     no_of_person, money_units = list(map(int,input().split()))
#     withdraw = list(map(int,input().split()))

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     while True:
#         List1 = list(map(int, input().split()))
#         List2 = list(map(int, input().split()))

'''
When you need to iterate through same index of both lists, you don't need to include nested loops.
You can refer index/value of another list with same i.
'''
# list1 = [0.896761,1.000000,1.000000,1.000000,1.000000,0.967020,0.896536,0.915352,0.928808,0.924341,1.000000]
# list2 = [0.891260,0.725591,0.863516,0.875115,0.864161,0.885342,0.892017,0.872830,0.879555,0.878611,0.866223]
# # List to store the results
# result = []

# # Iterate through both lists
# for i in range(len(list1)):
#     if list1[i] > list2[i] and list1[i] != 1:
#         difference = round(list1[i] - list2[i], 4)
#         result.append((list1[i], list2[i], difference))

# print(result)
# # Sort the result by the least difference
# result.sort(key=lambda x: x[2])

# print(result)