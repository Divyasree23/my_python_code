dict={1:"apple", 2:"orange", 3:"peer"}
#a = "apple"
def count_String(a):
    weight = 0
    for i in a:
        weight += ord(i)
    return weight

def countValueesInASCI(dict):
    weighted_dict = {}
    for i,v in dict.items():
        cnt_asci = count_String(v)
        weighted_dict[v] = cnt_asci
    return weighted_dict

print(countValueesInASCI(dict))
