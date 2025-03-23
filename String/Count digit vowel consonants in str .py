str = input()
vowel = "aeiouAEIOU"
cons , digi , vow = 0,0,0
for i in range(len(str)):
    if str[i].isdigit():
        digi += 1
    if str[i].isalpha():
        if str[i] not in vowel :
            cons += 1
        else:
            vow += 1 
print(cons,digi,vow)
