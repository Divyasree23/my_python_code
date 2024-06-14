#factorial Number
fact_num = 6
def fact_otpt(num):
    fact = 1
    if num == 0: ##range(num) = 0
        print(1)
    elif num < 0:
        print("given negative number")
    else:
        for i in range(1,num):
            fact = fact*i
        return fact

print(fact_otpt(fact_num))

Output:
120
