#find missed value
list=[1,4,8,9]
list1 = [6,7,9,13,1]
list2 = sorted(list1)
### it should be output=[2,5,6,7,8]

miss_value = []

def findMissValueInList(list):
    for i in range(list[0],list[-1]):
        if i not in list:
            miss_value.append(i)
    return miss_value

print(findMissValueInList(list))
print(findMissValueInList(list2))
