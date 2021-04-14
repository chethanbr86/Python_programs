#Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.
head = [1,4,3,2,5,2]
x = 3

#output = [1,2,2,4,3,5]

def partition(head, x):
    output = []
    for i in head:
        if i < x:
            head.pop(i)
            output.append(i)
        else:
            continue
    #print(head, output)
    return output

print(partition(head,x))

#unfinished
                

