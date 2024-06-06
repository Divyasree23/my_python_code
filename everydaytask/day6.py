list_ang = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Create an empty dictionary to hold our groups of anagrams

def findAnagramList(list_ang):
    anagram_dict = {}
    # Iterate through each word in the list
    for word in list_ang:
        key = ''.join(sorted(word))
        if key not in anagram_dict:
            anagram_dict[key] = [word]
        #print("key not in",key,anagram_dict)
        else:
            anagram_dict[key].append(word)
        #print("key in",key, anagram_dict)
    return anagram_dict
# Convert the values of the dictionary to a list of lists

result = findAnagramList(list_ang)
print(list(result.values()))

