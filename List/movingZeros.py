Num=[2,5,6,0,9,0,1]
#Output=[2,5,6,9,1,0,0]

#method1
newlist = [x for x in Num if x != 0 ]
zero_count = Num.count(0)
newlist_res = newlist + [0]*zero_count
print(newlist_res)

#method2
newlistwithoutZero = [x for x in Num if x != 0 ]
newlistwithZero = [x for x in Num if x == 0 ]
print(newlistwithoutZero+newlistwithZero)

#method3
def moveZeros(Num):
    r=0
    for i in range(len(Num)):
        if Num[i]:  #here will check if i = 0 returns false and swaping happens basically if 0: returns false
            Num[r],Num[i] = Num[i],Num[r]
            r += 1
    return Num
print(moveZeros(Num))

def moveZeros2(Num):
    j =0
    for i in range(len(Num)):
        if Num[i]!=0:
            Num[j]=Num[i]
            j +=1
    for k in range(j,len(Num)):
        Num[k]=0
    return Num

print(moveZeros2(Num))
