class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        totalBottles = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange
            totalBottles += newBottles
            emptyBottles = emptyBottles % numExchange + newBottles
        return totalBottles

print(Solution.numWaterBottles(9,3))