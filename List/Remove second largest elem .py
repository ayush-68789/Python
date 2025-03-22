lst = eval(input())
res = []
lst.sort()
for item in lst :
    if item not in res :
        res.append(item)
print(res[-2])
