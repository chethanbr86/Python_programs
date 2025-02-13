numBottles = 15
numExchange = 4

total_full = numBottles
total_exchange = numBottles

while total_exchange >= numExchange:    
    new_bottles = total_exchange // numExchange
    total_full = total_full + new_bottles
    total_exchange = new_bottles + (total_exchange % numExchange)

print(total_full)