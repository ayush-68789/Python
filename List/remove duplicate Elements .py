lst = eval (input())
res = []
for item in lst:
    if item not in res :
        res.append(item)
print(res)
