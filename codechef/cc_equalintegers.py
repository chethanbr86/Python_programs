# https://www.codechef.com/START41D/problems/INCREAR

#myway
# import time

# t = int(input())
# start_time = time.time()  # Start the timer

# for i in range(t):
#     x, y = list(map(int, input().split()))

#     x_counter = 0
#     y_counter = 0

#     while x != y:
#         if x > y:
#             y = y + 2
#             y_counter += 1
#         else:
#             x = x + 1
#             x_counter += 1
#     print(x_counter + y_counter)

# end_time = time.time()  # End the timer
# execution_time = end_time - start_time  # Calculate the execution time
# print(f"Execution time: {execution_time} seconds")

#AI solution
t = int(input())

for i in range(t):
    x, y = list(map(int, input().split()))

    if x >= y:
        diff = x - y
        if diff % 2 == 0:
            print(diff // 2)
        else:
            print(diff // 2 + 2)
    else:
        print(y - x)

#myway is right as well but AI solution take less time