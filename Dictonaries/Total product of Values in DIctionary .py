'''
TERMINAL :
Input Dictionary --- 
Enter Entry : 3
Enter Key : a
Enter Value : 12
Enter Key : b
Enter Value : 3
Enter Key : c
Enter Value : 4
Total Product :  144
'''


def user() :
    entry = int(input("Enter Entry : "))
    data = {}
    for i in range(entry):
        key = input("Enter Key : ")
        value = int(input("Enter Value : "))
        data[key] = value 
    return data
    
    
print("Input Dictionary --- ")
Dict = user()
multi = 1
for i in Dict.values():
    multi *= i
print("Total Product : ",multi)
