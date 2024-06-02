#Remove Duplicate values in given list

list=[1,2,4,4,5,6,6,7,7]

def removeDuplicatesFromList(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(removeDuplicatesFromList(list))
