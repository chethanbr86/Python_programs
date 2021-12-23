# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year%4 == 0 :	
	if year%400 == 0 and year%100 == 0:
		print('Leap')
	elif year%400 == 0:
		print('Leap')
	elif year%100 == 0:	
		print('Not Leap')
	else:
		print('Leap')
else:
	print('Not Leap')

#udemy way
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")


#tips and tricks: instead of repeating, go for multiple nested
