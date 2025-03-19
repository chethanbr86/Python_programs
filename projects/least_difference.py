#For kaggle
list1 = [0.896761,1.000000,1.000000,1.000000,1.000000,0.967020,0.896536,0.915352,0.928808,0.924341,1.000000]
list2 = [0.891260,0.725591,0.863516,0.875115,0.864161,0.885342,0.892017,0.872830,0.879555,0.878611,0.866223]

'''Need 2 outputs from 2 lists where difference between corresponding index values are least but the first value is greater than second and first value has a better score if not highest.
Meaning 1st priority is least difference and 2nd priority is highest value'''

# List to store the results
result = []

# Iterate through both lists
for i in range(len(list1)):
    if list1[i] > list2[i] and list1[i] != 1:
        difference = round(list1[i] - list2[i], 4)
        result.append((list1[i], list2[i], difference))

print(result)
# Sort the result by the least difference
result.sort(key=lambda x: x[2])

print(result)