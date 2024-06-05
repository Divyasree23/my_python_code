#"ababacdefgaba" substring "aba"
str="ababa"
substr="aba"

def countRepeatedSubString(str,substr):
    count = 0
    for i in range(0,len(str)-len(substr)+1):
        if str[i:i+len(substr)] == substr:
            count += 1
    return count

print(countRepeatedSubString(str,substr))
