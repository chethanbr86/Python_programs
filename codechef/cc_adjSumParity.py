#Logic
def logic_sol(C, N, B):
    for i in range(N):
        if C == 1 and B[i] == 1:
            C = 0
        elif C == 0 and B[i] == 1:
            C = 1
    return C 
    
def solution():
    N = int(input().strip())
    B = list(map(int, input().strip().split()))
    
    first = 1
    fe = logic_sol(1, N, B)
    
    if first == fe:
        print('YES')
        return
    
    first = 0
    fe = logic_sol(0, N, B)
    
    if first == fe:
        print('YES')
        return
    
    print('NO')
        
T = int(input().strip())        
while T > 0:
    T = T - 1
    solution()