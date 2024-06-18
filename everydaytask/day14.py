#checking given number is prime or not
given_number = 9999991

def primeNumber(givnum):
    strout = ""
    for i in range(2,givnum):
       if givnum % i == 0:
           strout = "Given is not a prime"
           break
    else:
        strout = "Given is prime"
    return strout

print(primeNumber(given_number))
