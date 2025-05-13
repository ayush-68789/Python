'''
TERMINAL :
Input Dictionary --- 
{'a' : 3 , 'b' : 2 }
6

'''


dict = eval(input())
prod = 1 
for i in dict.values() :
    prod *= i 
print(prod)
