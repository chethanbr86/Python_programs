# bank_balances = {}
# for bank, balance in ('', 0), ('hbank', 20), ('ibank', 25):
#     bank_balances[bank] = bank_balances.get(bank, 0) - balance  # removed - above in from_bank_summary and added - here
# for bank, balance in ('', 10), ('hbank', 40), ('ibank', 50):
#     bank_balances[bank] = bank_balances.get(bank, 0) + balance
# print(bank_balances.items())
# #debug in thonny

# class PrefixProduct:
#     def __init__(self):
#         self.prefix_product = [1]  # Initialize with 1 to handle the first product
#         self.size = 0

#     def append(self, num):
#         new_product = self.prefix_product[self.size] * num
#         self.prefix_product.append(new_product)
#         self.size += 1
#         print(self.prefix_product)

# # Example usage
# pp = PrefixProduct()
# pp.append(2)  # prefix_product becomes [1, 2]
# pp.append(3)  # prefix_product becomes [1, 2, 6]
# pp.append(4)  # prefix_product becomes [1, 2, 6, 24]
# pp.append(5)  # prefix_product becomes [1, 2, 6, 24, 120]
