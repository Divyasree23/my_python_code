#Find GCD = Greatest Common Divisor in a given list 
def findGcd(a,b):
    while b:  # stops when b = 0
        #print(b)
        a,b = b, a%b #56,42 = 42,14 #
    return a

def gcd_list(nums):
    gcd_result = nums[0]
    for num in nums[1:]:
        gcd_result = findGcd(gcd_result,num)
    return gcd_result

nums = [42,56,14,84]

result = gcd_list(nums)
print(f"The GCD of the list {nums} is: {result}")
