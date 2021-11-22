li = [5,3,8,2,4,6,10]
ran = [4,9]

new_li = 0

for i in li:
    if i >= ran[0] and i <= ran[1]:
        new_li = new_li + i
print(new_li)
