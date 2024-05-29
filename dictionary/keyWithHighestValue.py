# finding Key with the Highest Value from Dictionary
my_dict = {'a': 5, 'b': 9, 'c': 2}

def findMaxKey(my_dict):
    key,value = max(my_dict.items(),key = lambda x:x[1])
    return key # we can also print value here

output = findMaxKey(my_dict)
print("Highest value key is",output)