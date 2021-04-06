my_str = 'programming'

vow = ''
non_vow = ''

for i in my_str:
    if i in 'aeiou':
        vow = vow + i
    else:
        non_vow = non_vow + i

nwe_Str = vow + non_vow
print(nwe_Str)