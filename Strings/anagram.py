# Check if two strings are anagrams of each other.
# Examples: Input : str1 = “abcd”, str2 = “dabc” Output : True, both strings should have all values
str1 = "abcdef"
str2 = "efdcba1"

def anag(str1, str2):
    return sorted(str1) == sorted(str2)

print(anag(str1, str2))