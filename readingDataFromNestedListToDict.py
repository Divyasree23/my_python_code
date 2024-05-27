L = [['a', 1], ['b', 2], ['a', 3], ['c', 4],['b',5]]
D = {}

for i in range(len(L)):
    #print(L[i][0])
    if L[i][0] in D:#---->['a',1]['a']
        D[L[i][0]].append(L[i][1])
    else:
        D[L[i][0]] = []
        D[L[i][0]].append(L[i][1])

print(D)