#Nested sets (i.e., sets containing other sets) are not allowed in Python because sets require their elements to be hashable and immutable, while sets themselves are mutable and therefore not hashable. However, you can achieve similar functionality using frozensets, which are immutable sets and therefore can be elements of other sets. we will also have frozenset.

#Check if one set is a subset of another.
a = [[1],2,3,4,5,6]  ##checking list in list
b = [1]
def checkSubSet(a,b):
    if b not in a:
        print("busy buddy")
        print(a)
        print(b)
    else:
        print("false")
#print(b.issubset(a))
print(checkSubSet(a,b))

def is_subset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True

# Test cases
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(is_subset(set_a, set_b))  # Output: True

set_c = {1, 2, 6}
set_d = {1, 2, 3, 4, 5}
print(is_subset(set_c, set_d))  # Output: False