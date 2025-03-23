lst = eval(input())
n = len(lst)
for i in range(0,n):
    for j in range(0,n-i-1) :
        if (lst[j][1] < lst[j+1][1]):
            lst[j], lst[j+1] = lst[j+1] ,lst[j]
print(lst)
