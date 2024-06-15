#For a list, find the second largest number in the list.
my_nums = [44,11,83,29,25,76,85,88,87,90]
my_nums1 = sorted(my_nums)
print(my_nums1[-2])

def findSecondLargest(my_nums):
    fst_largest = my_nums[0]
    scd_largest = my_nums[0]
    for i in range(1,len(my_nums)):
        #print(my_nums[i])
        if my_nums[i] > fst_largest: #44,44
            scd_largest = fst_largest
            fst_largest = my_nums[i]
        elif my_nums[i] > scd_largest:
            scd_largest = my_nums[i]
    return scd_largest

abc = findSecondLargest(my_nums)
print(abc)
