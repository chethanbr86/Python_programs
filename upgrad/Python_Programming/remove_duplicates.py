# 1st way
l1 = [8,9,2,2,3,4,5,2]

l2= {}

for i in l1:
    if i not in l2:
        l2[i] = i
        print(l2)
print(list(l2.keys()))

#2nd way
l1 = [8, 9, 2, 2, 3, 4, 5, 2]

# In-place removal of duplicates using a for-loop on the same list.
# Iterate from the end toward the start so popping doesn't skip elements.
for i in range(len(l1) - 1, -1, -1):
    # print(range(len(l1) - 1, -1, -1))
    if l1[i] in l1[:i]:
        l1.pop(i)


print(l1)  # -> [8, 9, 2, 3, 4, 5]

# If you want to keep the last occurrence instead of the first, iterate forward and remove earlier duplicates (or use a set to track seen items).
# For large lists, this approach is O(n^2) due to slice membership checks; using a set/dict is O(n) (at the cost of extra memory).

