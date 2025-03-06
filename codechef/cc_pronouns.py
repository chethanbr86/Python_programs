#Codechef - myway 
# def Pronouns(S):
#     v = ['a','e','i','o','u']
#     if len(S) < 4:
#         print('Yes')
#     else:
#     # for i in range(0,len(S)-len(S)+4):  
#         for i in S[:3]:
#             if i in v:
#                 # def index_yes():
#                 index = []
#                 diff_list = []
#                 for i,j in enumerate(S):    
#                     if j in v:                        
#                         index.append(i)      
#                 if not index:
#                     print('No')
#                 # print(index)

#                 diff_list = []
#                 for i in range(1,len(index)):
#                     diff_list.append(index[i] - index[i-1])
#                     # return diff_list

#                 # y = index_yes()
#                 # print(y)
                
#                 for i in diff_list:
#                     if i > 4:
#                         print('No')
#                         break    #break is used to stop the loop if condition is true, else it will continue the loop and print yes at the end
#                 # else:
#                 print('Yes')
#                 break
#         else:
#             print('No')

# t = int(input())
# for _ in range(t):  
#     N = len(input())  
#     S = input()
#     Pronouns(S)

#Codechef - 1st way - vowel in word within a distance of 4 - failing hidden test case
# def Pronouns(S):
#     v = ['a','e','i','o','u']
#     if len(S) < 4:
#         print('Yes')
#     else: 
#         for i in S[:3]:
#             if i in v:
#                 index = []
#                 diff_list = []
#                 for i,j in enumerate(S):    
#                     if j in v:                        
#                         index.append(i)      
#                 if not index:
#                     print('No')

#                 diff_list = []
#                 for i in range(1,len(index)):
#                     diff_list.append(index[i] - index[i-1])               
                
#                 for i in diff_list:
#                     if i > 4:
#                         print('No')
#                         break    
#                 print('Yes')
#                 break
#         else:
#             print('No')

# t = int(input())
# for _ in range(t):  
#     N = len(input())  
#     S = input()
#     Pronouns(S)

'''
Logic I used against the required logic
 The logic within the if i in v: block is overly complex and doesn't correctly identify four or more consecutive consonants. 
 You're trying to find the difference between the indices of vowels, which isn't the right approach. 
 You should instead count consecutive consonants.
'''
'''
Solution Hint:
We run a loop through the string S and maintain a counter - 'count'
As we go through the loop, we use the following conditions:
If S[i] == 'a' OR 'e' OR 'i' OR 'o' OR 'u', then we reset value of count to 0
If S[i]≠ either of 'a' OR 'e' OR 'i' OR 'o' OR 'u', then we increment the counter as count = count + 1
It means that the loop as encountered 4 consecutive consonants
If value of count reaches 4, we should break out of the loop and output 'NO'
If value of count never reaches 4, we should output 'YES' 
'''

#Codechef - 2nd way - To not have more than 4 consonants in word within a distance of 4 - accepted
def Pronouns(S):
    v = ['a','e','i','o','u']
    count = 0
    for i in S:
        if i not in v:
            count += 1
            if count >= 4:
                print('No')
                break  
        else:
            count = 0                    
    else:
        print('Yes')  

t = int(input())
for _ in range(t):  
    N = len(input())  
    S = input().lower()
    Pronouns(S)