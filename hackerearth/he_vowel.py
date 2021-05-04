name2 = 'omahgoTuRuLob'
name3 = 'OmAhgotUrulobEI'
name4 = 'aeKORONAoiBATCHu'


name = [name2,name3,name4]
vow1 = 'aeiou' #try with list
vow2 = 'AEIOU'

def vowel(name, vow1, vow2):
    for i in name:
        # for j in vow:
        if vow1 in i or vow2 in i:
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