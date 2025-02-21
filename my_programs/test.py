# bank_balances = {}
# for bank, balance in ('', 0), ('hbank', 20), ('ibank', 25):
#     bank_balances[bank] = bank_balances.get(bank, 0) - balance  # removed - above in from_bank_summary and added - here
# for bank, balance in ('', 10), ('hbank', 40), ('ibank', 50):
#     bank_balances[bank] = bank_balances.get(bank, 0) + balance
# print(bank_balances.items())
# #debug in thonny

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
print(numbers)

my_list = [1]
size = 0

my_list.append(my_list[size]*numbers)
size += 1

print(my_list)
