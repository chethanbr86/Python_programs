def paperwork(n, m):
    return n*m if n > 0 and m > 0 else 0

print(paperwork(5, 2))
print(paperwork(-5, -2))
print(paperwork(-5, 2))
print(paperwork(5, 1))