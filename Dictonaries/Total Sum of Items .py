'''
TERMINAL :
Input Dictionary --- 
Enter Entry : 3
Enter Key : a
Enter Value : 3
Enter Key : b
Enter Value : 6
Enter Key : c
Enter Value : 8
Total sum :  17
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
total = sum(Dict.values())
print("Total sum : ",total)
