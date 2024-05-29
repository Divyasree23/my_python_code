#Define a function with takes two dictionaries and merge them and sum the values of common keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dict(dict1,dict2):
    for k,v in dict2.items():
        dict1[k] = dict1.get(k,0) + v ## to dict1, adding k from for loop
    return dict1

output = merge_dict(dict1,dict2)
print("Sum of similar keys in dictionary",output)

#getget() Method return the value for the given key if present in the dictionary.
# If not, then it will return None (if get() is used with only one argument).
#key: The key name of the item you want to return the value from
#Value: (Optional) Value to be returned if the key is not found.
# The default value is None.
#Syntax : Dict.get(key, default=None)

d = {1: '001', 2: '010', 3: '011'}
print(d.get(4)) #prints None
