class Water:
    def water_bottles(num_bottle, num_empty):
        # self.num_bottle = num_bottle
        # self.num_empty = num_empty
        total_empty = num_bottle
        untradeable = num_bottle%num_empty
        tradeable = total_empty - untradeable
        if tradeable > num_empty:
            num_bottle += 1
            print(total_empty, num_bottle, num_empty, tradeable, untradeable)

    water_bottles(10, 4)