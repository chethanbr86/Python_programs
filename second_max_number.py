my_list = [1, 7, -2, 0, 9, -1, 8, 11, 5]

def sec_lar(my_list):
    mini = float('-inf')
    first, sec = mini, mini
    for i in my_list:
        if i > first:
            first, sec = i, first
        elif first>i>sec:
            sec = i
    return sec if sec != mini else -1

m = sec_lar(my_list)
if m==-1:
    print('Not available')
else:
    print(m)

