#find min and max in list
#find min number and max number in given list
list = [203,9,89,3,76,75,100,91,101,2]

def findingMinMax(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max,min

print(findingMinMax(list))