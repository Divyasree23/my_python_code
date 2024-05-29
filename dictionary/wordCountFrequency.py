words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
dict={}

def wordCountFrequency(words):
    for i in words:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

print(wordCountFrequency(words))

