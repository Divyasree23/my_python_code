s1 = "abc"
s2 = "asgfhdbdsrgcadsf"

def findCharInWord(s,t):
    i=j=0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

print(findCharInWord(s1,s2))

