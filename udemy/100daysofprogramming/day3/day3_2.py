# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print('Welcome to BMI calculator')
BMI = round(weight/(height**2),2)
if BMI <= 18.5:
	print(f'Your BMI is {BMI}, you are underweight.')
elif BMI <= 25:
	print(f'Your BMI is {BMI}, you have a normal weight.')
elif BMI <= 30:
	print(f'Your BMI is {BMI}, you are slightly overweight.')
elif BMI <= 35:
	print(f'Your BMI is {BMI}, you are obese.')
else:
	print(f'Your BMI is {BMI}, you are clinically obese.')

#tips and tricks: elif bmi < 22 instead of if bmi>18 and bmi<22 