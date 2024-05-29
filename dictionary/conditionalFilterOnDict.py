my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,'e':5,'g':10}

def filterValueDivisible(my_dict):
    return {k:v for k,v in my_dict.items() if v%2 == 0}

output = filterValueDivisible(my_dict)
print("Dictionaries which values divisible by 2",output)