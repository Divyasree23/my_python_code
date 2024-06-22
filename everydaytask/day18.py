#Reverse string with mutiple words
def reverse_string(str):
    reverse = ""
    for char in str:
        reverse = char + reverse #just taking first value and appending it in backward direction
    return reverse

str = "be with positivity"
result = reverse_string(str)
print(str)
print(result)

#print words in string in reverse order
wstr = "show your courages will to sustain on your terms"
def reverseWordsInString(wstr):
    wstr1 = wstr.split()
    reverse_word = " "
    for word in wstr1:
        reverse_word = word + " " + reverse_word
    return reverse_word
print("given string of words: ",wstr)
print(reverseWordsInString(wstr))
