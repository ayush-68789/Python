n = int(input())
num = 1 
for i in range (0,n+1):
    for j in range (i):
        print(num,end="")
        num = num + 1 
        if (num > 9):
            num = 1 
    print()






'''


1 
2 3 
4 5 6 
7 8 9 1 
2 3 4 5 6




'''
