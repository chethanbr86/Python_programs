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

print(partition(head,x))


                

