num=[10,20,30,40,50,40,40,60,70]
start = 30
end = 70

def func(num,start,end):
    count_1 = 0
    for i in num:
        if start <= i <= end:
            count_1 += 1
    return count_1

print(func(num,start,end))