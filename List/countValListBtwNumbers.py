num=[10,20,30,40,50,40,40,88,60,70]
start = num.index(30)
end = num.index(70)
def func(num,start,end):
    count_1 = 0
    for i in range(len(num)):
        if start < i < end:
            count_1 += 1
    return count_1

print(func(num,start,end))
