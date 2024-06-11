#Problem 1:
input_list = [1,2,3,4,5,6,7,8,9,10]   # Example output: [4, 5, 1, 2, 3]
k=12
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    #print(k)
    #print(arr[-k:],arr[:-k])
    return arr[-k:] + arr[:-k]

# Example usage:
result = rotate_array(input_list, k)
print(result)  # Output: [4, 5, 1, 2, 3]

#output
#[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

#Problem 2:
#find the starting indices of all occurrences of the pattern in the string o/t [0,1]
str = "abracardabaacdefabr"
substr = "abr"
lst = []
for i in range(0,len(str)):
    if str[i:i+len(substr)] == substr:
        lst.append(i)
print(lst)
#Output : [0, 7, 16]
