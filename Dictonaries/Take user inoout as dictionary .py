def user(entries):
    data = {}
    for i in range(entries):
        key = input("Enter key : ")
        value =input("Enter Value : ")
        data[key] = value
    return data
    
entries = int(input("Enter the number of entries : "))
result = user(entries)
print("Resulting Dictionary : ")
print(result)


'''
Terminal :
Enter the number of entries : 5
Enter key : AT
Enter Value : 75
Enter key : AU
Enter Value : 96
Enter key : AV
Enter Value : 32
Enter key : AK
Enter Value : 12
Enter key : AQ
Enter Value : 96
Resulting Dictionary : 
{'AT': '75', 'AU': '96', 'AV': '32', 'AK': '12', 'AQ': '96'}

'''
