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
        print('No')
        return index

    m = index_yes()
    print(m)

    for i,j in enumerate(m):
        print(m[i])
#to be continued