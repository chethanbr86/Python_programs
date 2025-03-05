t = int(input())

for _ in range(t):    
    S = input()
    N = len(S)

if N < 4:
    print('Yes')
else:
    v = ['a','e','i','o','u']

    def index_yes():
        index = []
        for i,j in enumerate(S):    
            if j in v:                        
                index.append(i)      
        if not index:
            print('No')
        return index

    m = index_yes()
    print(m)

    #Difference between each list element
    diff_list = []
    def prefix_sum(list_b):
        for i in range(1,len(list_b)):
            diff_list.append(list_b[i] - list_b[i-1])
        return diff_list
    
    n = prefix_sum(m)
    print(n)
    
    for i in diff_list:
        if i > 3:
            print('No')
    else:
        print('Yes')
#i am getting solution but it is taking difference between vowel index, i also need to consider, differnt from 0 index to first vowel too

