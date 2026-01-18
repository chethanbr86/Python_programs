input_list = [1, 2, 4, 2, 3, 2, 3, 3, 6, 7]
key= 3  #output 4

index = -1
for i in range(len(input_list)):
    if input_list[i] == key:
        index = i
        break
print(index)