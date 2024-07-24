list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
#out=[3,4]

out = []
for i in list1:
    for j in list2:
        if i == j:
            out.append(i)
print(out)

out1 = [i for i in list1 if i in list2]
print(out1)


##Output
[3, 4]
[3, 4]
