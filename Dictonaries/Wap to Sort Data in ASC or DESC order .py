def dict_input(entries):
    data = {}
    for i in range(entries):
        key = input("Enter key : ")
        value = int(input("Enter Value : "))
        data[key] = value
    return data
    
    
def sort_data(data_input, ascending = True):
    return dict(sorted(data_input.items(), key=lambda item : item[1] , reverse = not ascending))

entries = int(input("Enter number of entries : "))
data_input = dict_input(entries)
print("Resulting Dictionary : ")
print(data_input)


sort_asc = sort_data(data_input, ascending = True)
print("Resulting Dictionary in ascending : ")
print(sort_asc)

sort_asc = sort_data(data_input, ascending = False)
print("Resulting Dictionary in descending : ")
print(sort_asc)


'''
Terminal : 
Enter number of entries : 5
Enter key : AT
Enter Value : 32
Enter key : AU
Enter Value : 30
Enter key : AS
Enter Value : 78
Enter key : AV
Enter Value : 55
Enter key : AX
Enter Value : 63
Resulting Dictionary : 
{'AT': 32, 'AU': 30, 'AS': 78, 'AV': 55, 'AX': 63}
Resulting Dictionary in ascending : 
{'AU': 30, 'AT': 32, 'AV': 55, 'AX': 63, 'AS': 78}
Resulting Dictionary in descending : 
{'AS': 78, 'AX': 63, 'AV': 55, 'AT': 32, 'AU': 30}



'''
