#life in weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#myway
'''
days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12

total_Days = int((90 * 365) - days)
total_Weeks = int((90 * 52) - weeks)
total_Months = int((90 * 12) - months)

print(f'You have {total_Days} days, {total_Weeks} weeks, and {total_Months} months left.')
'''

#udemy way
years_rem = 90 - int(age)

total_Days = years_rem * 365
total_Weeks = years_rem * 52
total_Months = years_rem * 12

print(f'You have {total_Days} days, {total_Weeks} weeks, and {total_Months} months left.')