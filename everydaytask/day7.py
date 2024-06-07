def reverse_vowels(str1):
    vowels = ""  # Variable to store vowels in their original order
    for char in str1:
        if char in "aeiouAEIOU":  # Check if the character is a vowel
            vowels += char  # Append the vowel to the vowels variable
    result_string = ""  # Variable to store the result string with reversed vowels
    for char in str1:
        if char in "aeiouAEIOU":  # Check if the character is a vowel
            result_string += vowels[-1]
            #print(result_string)# Append the last vowel from the vowels variable
            vowels = vowels[:-1]
            #print(vowels)# Remove the last vowel from the vowels variable
        else:
            result_string += char  # Append non-vowel characters as they are
    return result_string

print(reverse_vowels("opIniOn"))  #Opinion  -> Divya -- Davyi
