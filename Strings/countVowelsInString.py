str = "Your my world Happy beta"
def countVowels(str):
    vowels = 'aeiouAeiou'
    vowels_count = 0
    consnants = 0
    for char in str:
        if char in vowels:
            vowels_count += 1
        else:
            consnants += 1
    return vowels_count,consnants

result = countVowels(str)
print("Number of Vowels and consonants in a given string are",result[0],result[1])