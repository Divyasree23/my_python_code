#concatenate lists with numeric ranges using list comprehensions.
lst = [1,2,3,4,5,6,7]
lst1 = ['a','b','c','d','e','f','g']
x = [x for x in zip(lst,lst1)]
print(x)

### Example 1: Concatenate Multiple Ranges
combined_list = [num for num in range(5)] + [num for num in range(10, 15)] + [num for num in range(20, 25)]
print(combined_list)

### Example 2: Concatenate Ranges Dynamically
range_specs = [(0, 5), (10, 15), (20, 25)]
combined_list = [num for start, end in range_specs for num in range(start, end)]
print(combined_list)

### Example 3: Using Step Values
combined_list = [num for num in range(0, 10, 2)] + [num for num in range(10, 20, 3)]
print(combined_list)  # Output: [0, 2, 4, 6, 8, 10, 13, 16, 19]

### Example 4: Nested List Comprehensions for Complex Patterns
# Generate lists [0, 1], [10, 11], [20, 21] and concatenate them
combined_list = [num for i in range(3) for num in range(i * 10, i * 10 + 2)]
print(combined_list)  # Output: [0, 1, 10, 11, 20, 21]
