row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
cap = [row1, row2, row3]
print(cap)
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0]) #this is an example of taking inputs without split or giving inputs without comma
vertical = int(position[1])

# selected_row = cap[vertical-1]
# selected_row[horizontal-1] = "X"

#Instead of above 2 lines
cap[vertical-1][horizontal-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")