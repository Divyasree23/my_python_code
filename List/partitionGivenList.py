#Given a list and a value x, partition it such that all elements less than x come before elements greater than or equal to x.

list = [1,2,99,8,77,66,54,67,80,45,32,27]
list1 = sorted(list)
#print(list1) doing through loops
x = 40
def listPartition(list):
    new_min = []
    new_max = []
    for i in list:
        if i < x:
            new_min.append(i)
        if i > x:
            new_max.append(i)
    return new_min+new_max

print(listPartition(list))







