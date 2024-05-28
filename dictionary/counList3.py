li=[1,2,3,4,6,7,8,9,9,0,8,0,2,2,6,6,87,65,34,23]
count_dict ={}
for num in li:
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1
#print(count_dict)
mostReaptedValue = [num for num, count in count_dict.items() if count == 3 ]
print("3timesRepeatedValues",mostReaptedValue)