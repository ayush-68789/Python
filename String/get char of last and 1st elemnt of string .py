str = input()

if (len(str) < 2):
    res = ""
else:
    result1 = str[0:2]
    result2 = str[-2:]
    res = result1+ result2
print(res)
