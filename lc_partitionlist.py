#Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.
head = [1,4,3,2,6,5,2,6]
x = 3

#output = [1,2,2,4,3,5]

def partition(head, x):
    output = []
    for i in head:
        if i < x:            
            output.append(i)
            head.remove(i)
        else:
            continue
    output = output + head
    return output

# print(partition(head,x))

# Leetcode solution (not working here)
# def partition(head, x):
#     """
#     :type head: ListNode
#     :type x: int
#     :rtype: ListNode
#     """

#     # before and after are the two pointers used to create two list
#     # before_head and after_head are used to save the heads of the two lists.
#     # All of these are initialized with the dummy nodes created.
#     before = before_head = ListNode(0)
#     after = after_head = ListNode(0)

#     while head:
#         # If the original list node is lesser than the given x,
#         # assign it to the before list.
#         if head.val < x:
#             before.next = head
#             before = before.next
#         else:
#             # If the original list node is greater or equal to the given x,
#             # assign it to the after list.
#             after.next = head
#             after = after.next

#         # move ahead in the original list
#         head = head.next

#     # Last node of "after" list would also be ending node of the reformed list
#     after.next = None
#     # Once all the nodes are correctly assigned to the two lists,
#     # combine them to form a single list which would be returned.
#     before.next = after_head.next

#     return before_head.next

# print(partition([1,4,3,2,6,5,2,6],3))

                

