lst = eval(input())
for i in range(len(lst)-1):
    if (lst[i] +1 != lst[i+1]):
        miss = lst[i] + 1
print(miss)    
