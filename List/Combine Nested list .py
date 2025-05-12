lst = eval(input())
res = []
for item in lst :
    try  : 
        for j in item :
            res.append(j)
    except TypeError : 
        res.append(item)
print(res)
