t = int(input())
for _ in range(t):  
    N = len(input())  
    S = input()

v = ['a','e','i','o','u']
if len(S) < 4:
    print('Yes')
else:
# for i in range(0,len(S)-len(S)+4):  
    for i in S[:3]:
        if S[i] in v:
            def index_yes():
                index = []
                diff_list = []
                for i,j in enumerate(S):    
                    if j in v:                        
                        index.append(i)      
                if not index:
                    print('No')
                print(index)

                diff_list = []
                for i in range(1,len(index)):
                    diff_list.append(index[i] - index[i-1])
                return diff_list

            y = index_yes()
            print(y)
            
            for i in y:
                if i > 3:
                    print('No')
                    break    #break is used to stop the loop if condition is true, else it will continue the loop and print yes at the end
            else:
                print('Yes')
            break
    else:
        print('No')

        #Remaining: try to remove def in between and put input at end