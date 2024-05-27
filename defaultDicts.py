from collections import defaultdict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    merged_dict = defaultdict(int)

    # Add values from dict1
    for key, value in dict1.items():
        merged_dict[key] += value

    # Add values from dict2
    for key, value in dict2.items():
        merged_dict[key] += value

    # Convert defaultdict back to a regular dictionary
    return dict(merged_dict)

print(merge_dicts(dict1,dict2))