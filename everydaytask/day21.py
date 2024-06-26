#How would you capitalize the first letter of each word in a string?

str = "be happy in your world"
lst  = str.title()
print(lst)

str2 = []
for word in str.split():
    str2.append(word.capitalize())
print(' '.join(str2))


#Write a function to check if a string contains only digits.
num_str = "6679064555"

for i in num_str:
    if i < '0' or i > '9':
        str3 = "string contains alphabets as well"
        break
    else:
        str3 = "string contains only digits"
print(str3)

if num_str.isdigit():
    str4 = "string contains only digits"
else:
    str4 = "string contains alphabets as well"
print(str4)
