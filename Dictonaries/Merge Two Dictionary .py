'''
TERMINAL : 
Input Dictionary 1 --- 
Enter Entry : 2
Enter Key : A
Enter Value : 1
Enter Key : B
Enter Value : 2
Input Dictionary 2 --- 
Enter Entry : 3
Enter Key : C
Enter Value : 4
Enter Key : D
Enter Value : 6
Enter Key : E
Enter Value : 7
Merged Dictionary is : 
 {'A': 1, 'B': 2, 'C': 4, 'D': 6, 'E': 7}

 '''
def user() :
    entry = int(input("Enter Entry : "))
    data = {}
    for i in range(entry):
        key = input("Enter Key : ")
        value = int(input("Enter Value : "))
        data[key] = value 
    return data
    
    
print("Input Dictionary 1 --- ")
Dict1 = user()
print("Input Dictionary 2 --- ")
Dict2 = user()
merge = Dict1.copy()
merge.update(Dict2)
print("Merged Dictionary is : \n",merge)
