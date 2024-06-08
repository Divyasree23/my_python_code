str=["egg","swim","walk","run","jump","dance"]
#output:- ['dance', 'jump', 'run','swim','walk']
n = len(str)

def swapWordsInAscendingOrder(str):
    n = len(str)
    for i in range(n):
        for j in range(n-i-1):
            #print(n, i, j, str[j], str[j + 1], str)
            if str[j] > str[j+1]:
                str[j],str[j+1]=str[j+1],str[j]
    return str

result = swapWordsInAscendingOrder(str)
print(result)
