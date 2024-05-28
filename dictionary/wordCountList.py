words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
word={}
def word_dict(words):
    for i in words:
        if i not in word:
            word[i] = 1
        else:
            word[i] =+ 1
    return word

print(word_dict(words))