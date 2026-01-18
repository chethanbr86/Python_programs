ar = 9, 11, 13
k = 19  #output False

d = ar[1] - ar[0]

for i in range(len(ar)):
    if (k - ar[i]) % d != 0:
        print(False)
        break
    print(True)
    break

