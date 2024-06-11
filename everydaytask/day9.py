input_list = [1,2,3,4,5,6,7,8,9,10]   # Example output: [4, 5, 1, 2, 3]
k=12
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    #print(k)
    print(arr[-k:],arr[:-k])
    return arr[-k:] + arr[:-k]

# Example usage:
result = rotate_array(input_list, k)
print(result)  # Output: [4, 5, 1, 2, 3]
