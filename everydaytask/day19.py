#Decimal to Binary Format
def dec_to_binary(num):
    lst = []
    while num > 0:
        lst.append(num%2)
        #print(num%2) #1
        num = num//2
    lst1 = lst[::-1]
    bnry = ''
    for k in lst1:
        bnry += str(k)
    return bnry

print(dec_to_binary(5))
print(dec_to_binary(78))
#output
#101
#1001110
