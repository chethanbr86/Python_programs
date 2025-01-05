# class Solution:
#     def numWaterBottles(numBottles, numExchange):
#         # self.numBottles = numBottles
#         # self.numExchange = numExchange
#         total_full = numBottles
#         numExchange = numBottles
#         while numBottles >= numExchange: #numBottles//numExchange != 0:
#             total_full = numBottles + numBottles//numExchange
#             numExchange = numBottles//numExchange + numBottles%numExchange
#         return total_full

# Solution.numWaterBottles(10, 4)

# x = input()
# my_list = x.split(' ')
# numBottles = int(my_list[0])
# numExchange = int(my_list[1])
numBottles = int(input())
numExchange = int(input())

total_full = 0
# numExchange = numBottles
while numBottles//numExchange != 0:
    total_full = numBottles
    total_full = numBottles + numBottles//numExchange
    numExchange = numBottles//numExchange + numBottles%numExchange
    print(total_full)
    #not complete