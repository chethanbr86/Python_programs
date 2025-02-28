# t = int(input().strip())

# list_a = [] 
# for i in range(t):
#     n = int(input().strip())
#     a = list(map(int,input().strip().split(',')))
#     list_a.append(a)
# print(list_a)

# list_a = [[1,2],[1,2,3],[1,100,10]]

#max element
# def max_element():
#     for i in list_a:
#         max_ele = i[0]
#         for j in i:
#             if j > max_ele:
#                 max_ele = j
#             else:            
#                 i.remove(j)
#         print(max_ele)
#         return max_ele

# for i in list_a:
#     # max_element = i[0]
#     for j in range(len(i)-1):
#         if i[j-1] != max_element or i[j] != max_element:
#             if i[j] < i[j+1]:
#                 list_a[j] = i[j+1] - i[j]
#             else:
#                 list_a[j] = i[j] - i[j+1]
# print(list_a)

# Making nested list into separate lists
# for i in range(len(list_a)):
#     cur_index_value = list_a[i]
#     print(cur_index_value)
            
#Codechef solution
# def electric(incident):
#     Nat= len(incident)
#     nolan = 0
#     for Mud in range(Nat):
#         neil = incident[Mud]
#         jig=0
#         if Mud>0:
#             jig=incident[Mud-1]
#             for i in range(Mud-2, -1,-1):
#                 gud = max(0, jig - incident[i])
#                 lop = max(0, incident[i] - jig)
#                 jig = min(gud, lop)
#         if Mud>0:
#             gud = max(0, neil - jig)
#             lop = max(0, jig - neil)
#             neil = max(gud, lop)
#         oil = 0
#         if Mud < Nat - 1:
#             oil=incident[Mud+1]
#             for i in range(Mud+2,Nat):
#                 gud=max(0, oil - incident[i])
#                 lop=max(0, incident[i] - oil)
#                 oil = min(gud, lop)
#         if Mud<Nat-1:
#             gud=max(0, neil - oil)
#             lop=max(0, oil - neil)
#             neil=max(gud, lop)
            
            
#         if neil > nolan:
#             nolan = neil
#     return nolan
    
# T= int(input())
# for _ in range(T):
#     Nat = int(input())
#     incident = list(map(int, input().split()))
#     tiss = electric(incident)
#     print(tiss)

# Decoding codechef sol in myway
# def list_slime(a):
#     target_value = 0
#     for i in range(len(a)):
#         cur_index_value = a[i]
#         prev_index_value = 0

#         if i > 0:
#             prev_index_value = a[i-1] 
#             for j in range(i-2,-1,-1):
#                 k = max(0, prev_index_value-a[j])
#                 l = max(0, a[j] - prev_index_value)
#                 prev_index_value = min(k,l)

#         if i > 0:
#             k = max(0, cur_index_value - prev_index_value)
#             l = max(0, prev_index_value - cur_index_value)
#             cur_index_value = max(k,l)

#         next_index_value = 0
#         if i < len(a) - 1:
#             next_index_value = a[i+1]
#             for j in range(i+2, len(a)):
#                 k = max(0, next_index_value - a[j])
#                 l = max(0, a[j] - next_index_value)
#                 next_index_value = min(k,l)

#         if i < len(a) - 1:
#             k = max(0, cur_index_value - next_index_value)
#             l = max(0, next_index_value - cur_index_value)
#             cur_index_value = max(k,l)

#         if cur_index_value > target_value:
#             target_value = cur_index_value

#     return target_value

# t = int(input())
# for i in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     new_list = list_slime(a)
#     print(new_list)

# def list_slime(a):
#     n = len(a)
#     if n == 1:
#         return a[0]  # Only one element, return it directly

#     # Left modification (prefix min-reduction)
#     left = [0] * n
#     left[0] = a[0]
#     for i in range(1, n):
#         diff = abs(left[i-1] - a[i])
#         left[i] = max(0, min(left[i-1], diff))

#     # Right modification (suffix min-reduction)
#     right = [0] * n
#     right[-1] = a[-1]
#     for i in range(n-2, -1, -1):
#         diff = abs(right[i+1] - a[i])
#         right[i] = max(0, min(right[i+1], diff))

#     # Find max possible cur_index_value by combining both sides
#     max_value = 0
#     for i in range(n):
#         cur_index_value = a[i]
#         if i > 0:
#             cur_index_value = max(cur_index_value, abs(cur_index_value - left[i-1]))
#         if i < n - 1:
#             cur_index_value = max(cur_index_value, abs(cur_index_value - right[i+1]))
#         max_value = max(max_value, cur_index_value)

#     return max_value


# # Reading input
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(list_slime(a))

#Chatgpt optimized solution 1
# def list_slime(a):
#     n = len(a)
#     target_value = 0

#     # Left prefix array to track reductions
#     left_min = [0] * n
#     if n > 1:
#         left_min[0] = a[0]
#         for i in range(1, n):
#             left_min[i] = min(left_min[i-1], abs(left_min[i-1] - a[i]))

#     # Right suffix array to track reductions
#     right_min = [0] * n
#     if n > 1:
#         right_min[-1] = a[-1]
#         for i in range(n-2, -1, -1):
#             right_min[i] = min(right_min[i+1], abs(right_min[i+1] - a[i]))

#     # Compute the maximum value by combining left and right reductions
#     for i in range(n):
#         cur_index_value = a[i]

#         # Adjust based on left-side values
#         if i > 0:
#             cur_index_value = max(0, abs(cur_index_value - left_min[i-1]))

#         # Adjust based on right-side values
#         if i < n-1:
#             cur_index_value = max(0, abs(cur_index_value - right_min[i+1]))

#         # Track the maximum possible cur_index_value
#         target_value = max(target_value, cur_index_value)

#     return target_value

# # Reading input
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(list_slime(a))

#chatgpt optimized solution 2
def list_slime(a):
    # n = len(a)
    max_result = 0

    for i in range(len(a)):
        cur_index_value = a[i]

        # Calculate left modification
        if i > 0:
            prev_index_value = a[i - 1]
            for j in range(i - 2, -1, -1):
                prev_index_value = max(0, min(prev_index_value - a[j], a[j] - prev_index_value))
            cur_index_value = max(0, max(cur_index_value - prev_index_value, prev_index_value - cur_index_value))

        # Calculate right modification
        if i < len(a) - 1:
            next_index_value = a[i + 1]
            for j in range(i + 2, len(a)):
                next_index_value = max(0, min(next_index_value - a[j], a[j] - next_index_value))
            cur_index_value = max(0, max(cur_index_value - next_index_value, next_index_value - cur_index_value))

        max_result = max(max_result, cur_index_value)

    return max_result

# Reading input
t = int(input())  # Number of test cases
for _ in range(t):
    n = int(input())  # Size of list
    a = list(map(int, input().split()))  # Input list
    print(list_slime(a))

#chatgpt solution 1 and 2 optimized to o(n) rather than codechef solution o(n^2)