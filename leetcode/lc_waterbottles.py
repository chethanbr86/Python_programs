class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        self.numBottles = numBottles
        self.numExchange = numExchange

        total_full = numBottles
        total_exchange = numBottles

        while total_exchange >= numExchange:    
            # new_bottles = total_exchange // numExchange
            total_full = total_full + (total_exchange // numExchange)
            total_exchange = (total_exchange // numExchange) + (total_exchange % numExchange) #i was taking total_full in numerator instead of total_exchange

        return total_full
    
solution = Solution()
result = solution.numWaterBottles(15,4)
print(result)