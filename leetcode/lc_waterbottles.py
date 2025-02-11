numBottles = 10
numExchange = 3

total_full = numBottles
total_exchange = numBottles // numExchange
while total_exchange != 0:    
    total_full = numBottles + (numBottles // numExchange)
    total_exchange = (numBottles // numExchange) + (numBottles % numExchange)

print(total_full, total_exchange)
#not complete