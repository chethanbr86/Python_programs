numBottles = 15
numExchange = 4

total_full = 0
total_exchange = 0
while total_exchange < numExchange:    
    total_full = numBottles + (numBottles // numExchange)
    total_exchange = (total_full // numExchange) + (total_full % numExchange)

print(total_full, total_exchange)
#not complete