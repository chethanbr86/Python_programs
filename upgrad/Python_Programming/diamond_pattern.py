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

'''

    *
   *_*
  *_*_*
 *_*_*_*
*_*_*_*_*

'''

#please take input here
n = int(input())

#start writing your code here
if 1<=n<=20:
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end='')
        for k in range(i-1):
            print('*_',end='')
        print('*')