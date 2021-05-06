# from geeksforgeeks

my_list = [1,2,3,4,5]
k = 2

new_list = []
for i,x in enumerate(my_list):
    new_list.append(my_list[(i+3)%len(my_list)])
print(new_list)

# Learn how to take input from hackerearth problem
#1
#5 2 
#1 2 3 4 5