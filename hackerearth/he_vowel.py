name2 = 'omahgoTuRuLob'
name3 = 'OmAhgotUrulobEI'
name4 = 'aeKORONAoiBATCHu'


name = [name2,name3,name4]
vow1 = ['A','E','I','O','U']
vow2 = ['a','e','i','o','u']

def vowel(name, vow1, vow2):
    for i in range(len(name)):
        # for j in vow:
        if name[i] in vow1 or name[i] in vow2:  
            return 1
        else:
            return 0


m = vowel(name, vow1, vow2)
for i in name:
    if m == 1:
        print('lovely string')
    else:
        print('ugly string')

#unsolved