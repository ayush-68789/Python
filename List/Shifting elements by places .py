lst = eval(input())
n = int(input("Enter places of shift : "))
result = []*len(lst)

if n > 0 :       #right shifting
    result = lst[-n:] + lst[:-n]
    print(result)
if n < 0 :       #left shifitng 
    result = lst[-n:] + lst[:-n]
    print(result)

'''
# TERMINAL 

[1,2,3,4,5,6,7,8,9]
Enter places of shift : 2   (right shift)
[8, 9, 1, 2, 3, 4, 5, 6, 7]


[1,2,3,4,5,6,7,8,9]
Enter places of shift : -2   (left shift)
[3, 4, 5, 6, 7, 8, 9, 1, 2]


''''
