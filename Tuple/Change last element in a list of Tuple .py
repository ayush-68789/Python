tup = eval(input())
num = int(input())
res = []
new_tup =()
for item in tup :
    new_tup = item[:-1] + (num,)
    res.append(new_tup)
print(res)
