lst = eval(input())
target = int(input())
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if (lst[i] + lst[j] == target):
            print([i, j])
            break
