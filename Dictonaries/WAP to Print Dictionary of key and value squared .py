'''
TERMINAL : 
Enter entry : 5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''


dict = {}
entry = int(input())
for i in range (1,entry+1) :
    dict[i] = i*i 
print(dict)
