#For kaggle
list1 = [0.896761,1.000000,1.000000,1.000000,1.000000,0.967020,0.896536,0.915352,0.928808,0.924341,1.000000]
list2 = [0.891260,0.725591,0.863516,0.875115,0.864161,0.885342,0.892017,0.872830,0.879555,0.878611,0.866223]

'''Need 2 outputs from 2 lists where difference between corresponding index values are least but the first value is greater than second and first value has a better score if not highest.
Meaning 1st priority is least difference and 2nd priority is highest value'''

def biggest_value(List):
    for i in range(1,len(List)):
        if List[i] == float(1):
            i += 1
        else:
            pass

        

list3 = []
for i in range(1,len(list1)):
    for j in range(len(list2)):
        if list1[i] < list2[j]:
            list1[i] += 1
            list2[j] += 1
        else:

            list3.append([list1[i],list2[j]])
print(list3)