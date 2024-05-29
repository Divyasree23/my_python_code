#Reverse key with value, value with key
my_dict = {'a': 1, 'b': 2, 'c': 3}

def reverseKeyValue(my_dict):
    return {k:v for v,k in my_dict.items()}

output = reverseKeyValue(my_dict)
print("Reversed dict with values,key",output)