'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
n=5
# for i in range(n):
#     for j in range(i+1):
#         print('* ', end=' ')
#     print('\r')  #ending line after each row with \r, it can just be print() too

#or using list
# myList = []
# for i in range(1,n+1):
#     myList.append("* "*i)
# print("\n".join(myList))

#or 
for i in range(n):
    print(('* '+' ')*(i+1))