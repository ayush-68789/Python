lst = eval(input())
k = int(input())

l = len(lst)
k = k % l 

if k > 0 :
    res = lst[-k:] + lst[:-k]
    print(res)
else:
    print(res)
    
