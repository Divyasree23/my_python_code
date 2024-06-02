#Swap two elements in a tuple.
#We can't change created tuple as it is immutable, so we have to convert tuple into List and swap the values.
tple1 = (1,2,5,6,7,8)
tple1 = list(tple1)
def tple(tple1,ind,ind1):
    t=tple1[ind],tple1[ind1]
    tple1[ind1],tple1[ind]=t
    return tple1

print(tple(tple1,0,2))

t = (1, 2, 3, 4, 5)
i, j = 1, 3  # Indices of the elements you want to swap
# Convert the tuple to a list
temp_list = list(t)
temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
swapped_tuple = tuple(temp_list)
print(swapped_tuple)  # Output: (1, 4, 3, 2, 5)