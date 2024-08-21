#explode nested list
lis=[1,2,3,[4,5],6,[7,8,[9,2]],10]

def nestedFunc(lis):
    lst1 = []
    for num in lis:
        if isinstance(num,list):
            lst1.extend(nestedFunc(num))
        else:
            lst1.append(num)
    return lst1

print(nestedFunc(lis))
