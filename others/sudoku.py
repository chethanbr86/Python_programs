# row1 = ["\'x\',"*10]
#fill random numbers
row1 = [0, 5, 0, 0, 0, 0, 1, 0, 0]
row2 = [0, 0, 0, 3, 0, 2, 0, 0, 0]
row3 = [0, 6, 0, 0, 0, 7, 0, 0, 0]
row4 = [0, 0, 4, 0, 0, 1, 0, 0, 0]
row5 = [8, 0, 0, 0, 0, 0, 0, 4, 0]
row6 = [0, 3, 0, 0, 0, 0, 5, 0, 0]
row7 = [0, 0, 8, 5, 0, 0, 0, 0, 0]
row8 = [2, 0, 0, 0, 0, 0, 0, 0, 7]
row9 = [0, 0, 0, 4, 0, 0, 0, 1, 0]

map = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
position = input("Where do you want to put the treasure? ")
number = int(input('Which number do you want to fill? '))

horizontal = int(position[0]) #this is an example of taking inputs without split or giving inputs without comma
vertical = int(position[1])

if map[vertical-1][horizontal-1] == 0:
    map[vertical-1][horizontal-1] = number
else:
    print('position is already filled')

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}")