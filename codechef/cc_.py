# Example of how to take input

# Read the number of test cases
T = int(input().strip())

for _ in range(T):
    # Read the size of the array
    N = int(input().strip())
    
    # Read the array as a list of integers
    A = list(map(int, input().strip().split(',')))
    
    # Process the input (Example: Print the array)
    print(f"Test case {_+1}: N={N}, A={A}")
