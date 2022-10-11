import random
# chethan, nayana, sharadhy, digu, indu, chandu, bhagu
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
print(len(names))

# print(random.choice(names))

name = random.randint(0,len(names)-1)
print(name)
print(names[name][0].upper()+names[name][1:]+' is going to pay for party today!')

#Make an app