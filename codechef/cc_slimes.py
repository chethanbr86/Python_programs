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
#     first_value = list_a[i]
#     print(first_value)
            
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
def list_slime(a):
    target_value = 0
    for i in range(len(a)):
        first_value = a[i]
        target_index = 0

        if i > 0:
            target_index = a[i-1] 
            for j in range(i-2,-1,-1):
                k = max(0, target_index-a[j])
                l = max(0, a[j] - target_index)
                target_index = min(k,l)

        if i > 0:
            k = max(0, first_value - target_index)
            l = max(0, target_index - first_value)
            first_value = max(k,l)

        m = 0
        if i < len(a) - 1:
            m = a[i+1]
            for j in range(i+2, len(a)):
                k = max(0, m - a[j])
                l = max(0, a[j] - m)
                m = min(k,l)

        if i < len(a) - 1:
            k = max(0, first_value - m)
            l = max(0, m - first_value)
            first_value = max(k,l)

        if first_value > target_value:
            target_value = first_value

    return target_value

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    new_list = list_slime(a)
    print(new_list)