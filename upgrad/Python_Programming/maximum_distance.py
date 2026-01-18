input_list = [1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]  #output 8

def max_distance(input_list,n):
    my_dict = {}
    max_dist = 0

    for k in range(n):
        if input_list[k] not in my_dict.keys():
            my_dict[input_list[k]] = k
    
        else:
            max_dist = max(max_dist,k-my_dict[input_list[k]])
    
    return max_dist


m = input_list
n = len(input_list) 

print(max_distance(m,n))