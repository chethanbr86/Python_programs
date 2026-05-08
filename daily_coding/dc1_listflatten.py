my_list = [[10, 15], [12, 15, 20, 34], [17, 20, 32]]

# my_list_1 = my_list[0]
# my_list_2 = my_list[1]
# my_list_3 = my_list[2]
# print(sorted(my_list_1+my_list_2+my_list_3))

# new_lsit = []
# for i in my_list:
#     for j in i:
#         new_lsit.append(j)
# print(sorted(new_lsit))
#The time complexity for that would be O(KN log KN), since we have K * N total elements.

#Daily coding problem solution:
import heapq #heaps are great for finding smallest numbers

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

print(merge(my_list))
# The time complexity for this would be O(KN log K), since we remove and append to the heap K * N times.