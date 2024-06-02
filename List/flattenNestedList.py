#Flatten nested list
lst = [[1,2,3,4,5],[6,7,8,9],'a','b',10,11]
flatten_list = []

def flattenStrings(lst): ## it will flattten integer and string both
    for i in lst:
        if isinstance(i,list):
            flatten_list.extend(i)
        else:
            flatten_list.append(i)
    return flatten_list

print(flattenStrings(lst))


def flatten(lst): ## it will flattten only integer
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))  # Recursive call for nested lists
        else:
            flattened_list.append(item)  # Directly append non-list items
    return flattened_list


lst = [[1, 2, 3, 4, 5], [6, 7, 8, 9], 10, 11]
print(flatten(lst))