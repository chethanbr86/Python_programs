# Leetcode solution
class ProductOfNumbers:
    # Stores cumulative product of the stream
    def __init__(self):
        # Initialize the product list with 1 to handle multiplication logic
        self.prefix_product = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            # If num is 0, reset the cumulative products since multiplication
            # with 0 invalidates previous products
            self.prefix_product = [1]
            self.size = 0
        else:
            # Append the cumulative product of the current number with the last
            # product
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        # Check if the requested product length exceeds the size of the valid
        # product list
        if k > self.size:
            return 0
        # Compute the product of the last k elements using division
        return self.prefix_product[self.size] // self.prefix_product[self.size - k]

# multiple input in a line
obj = ProductOfNumbers()
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(x) for x in numbers]
k = int(input("Enter the value of k: "))

for num in numbers:
    obj.add(num)

param_2 = obj.getProduct(k)
print(param_2)