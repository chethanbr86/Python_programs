'''
[1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
[2] If width and height, both are large enough and
(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
(b) else user is prompted to crop it. Print "CROP IT" in this case.
'''

inp = list(map(int,input().split()))
l = inp[0]
n = inp[1]
w = inp[2]
h = inp[3]

for i in range(n):
    if w < l or h < l:
        print('UPLOAD ANOTHER')
    elif w == l and h == l:
        print('ACCEPTED')
    else:
        print('CROP IT')

#infinite loop, fix it