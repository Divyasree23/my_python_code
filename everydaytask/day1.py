phrase = "big black bug bit a big black dog on his on big black nose"
words = phrase.split(' ')
#print(phrase1)
dict={}

def countRepeatedWordsInString(words):
    for k in words:
        if k in dict:
            dict[k] += 1
        else:
            dict[k] = 1
    return dict
print(countRepeatedWordsInString(words))

for k,v in dict.items():
    print(k,v)
