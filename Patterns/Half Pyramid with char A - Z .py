n = int(input())
char = ord('A') 
for i in range (0,n+1):
    for j in range (i):
        print(chr(char),end="")
        char = char + 1 
        if (char > ord('Z')):
            char = ord('A') 
    print()


'''


A
BC
DEF
GHIJ
KLMNO



'''
