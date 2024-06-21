#LCM  calculate the least common multiple (LCM) with n list values.
def calculate_lcm(x, y):
    c = x*y
    for i in range(1, c + 1):
        if i % x == 0 and i % y == 0:
            break
    return i

def lcm_list(nums):
    lcm_result = nums[0]
    for num in nums[1:]:
        lcm_result = calculate_lcm(lcm_result,num)
    return lcm_result

nums = [67,93,54,108] #330, 75, 450, 225
result = lcm_list(nums)
print(f"The LCM of the list {nums} is: {result}")
