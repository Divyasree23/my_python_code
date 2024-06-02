nested_dict = {'a': {'b': {'c': 42}}}
keys = ['a', 'b', 'c']

def get_nested_value(d, keys):  ##best solution
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return None
    return d

result = get_nested_value(nested_dict, keys)
print(result)

def nest_function(nested_dict,keys):
    for key in keys:
        nested_dict=nested_dict[key]
        #print(nested_dict)
    return nested_dict

print(nest_function(nested_dict,keys)) 

def nestFunctionFor(nested_dict):
    for i,j in nested_dict.items():
        for x,y in j.items():
            for z,a in y.items():
                res = a
    return a
print(nestFunctionFor(nested_dict))