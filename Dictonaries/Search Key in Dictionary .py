'''
TERMINAL : 
Enter Entries : 2
Enter Key : A
Enter Value : 14
Enter Key : B
Enter Value : 13
{'A': 14, 'B': 13}
Enter key you want to check : B
True

'''

# CODE  : 
dict = eval(input())
key = input()
if key in dict : 
    print ("Found")
else :
    print("Not Found")
