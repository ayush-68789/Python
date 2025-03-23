tup = eval(input())
rem = int(input())
res = ()
for item in tup :
    if item != rem:
        res += (item,)
print(res)
