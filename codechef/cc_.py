# Example of how to take inputs

# 3 = T
# 4 = N (number of element within the list)
# 2,3,4,5
# Test case 1: N=4, A=[2, 3, 4, 5]
# 6
# 1,3,5,9,7,8  
# Test case 2: N=6, A=[1, 3, 5, 9, 7, 8]
# 1
# 3
# Test case 3: N=1, A=[3]

# Read the number of test cases
T = int(input().strip())

for _ in range(T):
    # Read the size of the array
    N = int(input().strip())
    
    # Read the array as a list of integers
    A = list(map(int, input().strip().split(',')))
    
    # Process the input (Example: Print the array)
    print(f"Test case {_+1}: N={N}, A={A}")


#2
#If you know exact number of inputs in a line
# 4
# 10 20 30 = d1
# 30 20 10 = s1
# 5 23 87 = d2
# 5 23 87 = s2
# 0 15 100 = d3
# 100 5 5 = s3

# T = int(input().strip())
# print(T)

# for _ in range(T):
#     D1, D2, D3 = list(map(int,input().split()))
#     S1, S2, S3 = list(map(int,input().split()))
#     T_Dragon = D1 + D2 + D3
#     T_Sloth = S1 + S2 + S3
#     print(D1,D2,D3)
#     print(S1,S2,S3)
#     print(f'T_Dragon {T_Dragon}')
#     print(f'T_Sloth {T_Sloth}')