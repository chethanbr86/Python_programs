'''
    * 
   * * 
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

n = 5
for i in range(n):
    print(' '*(n-i-1)+('* ')*(i+1)) #or ('*'+' ')
for j in range(n-1):
   print(' '*(j+1)+('* ')*(n-j-1))