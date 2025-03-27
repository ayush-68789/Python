def dict_input(entries):
    data = {}
    for i in range(entries):
        key = input("Enter key : ")
        value = int(input("Enter Value : "))
        data[key] = value
    return data
    
def update(data_input):
    new_key = input("Enter New key : ")
    new_value = int(input("Enter New Value : "))
    data_input[new_key] = new_value
    return data_input
    
    
entries = int(input("Enter number of entries : "))
data_input = dict_input(entries)
print("Resulting Dictionary : ")
print(data_input)
 
updated = update(data_input)
print("Updated Dictionary : ")
print(updated)


'''
Terminal : 
Enter number of entries : 2
Enter key : AT
Enter Value : 32
Enter key : AU
Enter Value : 30
Resulting Dictionary : 
{'AT': 32, 'AU': 30}
Enter New key : AS
Enter New Value : 38
Updated Dictionary : 
{'AT': 32, 'AU': 30, 'AS': 38}

'''
