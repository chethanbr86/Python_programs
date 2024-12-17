#count how many elements in the list
t = [0,1,2,2,3,0,5,7,6,5,2]
hist = {}
for x in t:
    hist[x] = hist.get(x, 0) + 1
print(hist)