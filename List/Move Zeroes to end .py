lst = eval(input())
res = []

count = 0 
for item in lst :
    if item != 0 :
        res.append(item)
    else :
        count += 1
zero = [0] * count
print(res+zero)
