from tqdm import tqdm, trange

s = 'abcabcbb'
#output = 3 #abc with length of 3

# Below code is just to find substring
l = []
for i in tqdm(range(len(s)), desc='outer loop'):
    for j in tqdm(range(i+1,len(s)+1), desc='inner loop'):
        l.append(s[i:j])
print(l)

# Real code yet to begin
    

