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
def user(entries):
    data = {}
    for i in range(entries):
        key = input("Enter Key : ")
        value = int(input("Enter Value : "))
        data[key] = value 
    return data

def search_key(dictionary , key):
    if key in dictionary :
        return True
        
    else:
        return False
        
    
def main():
    entries = int(input("Enter Entries : "))
    result = user(entries)
    print(result)
    key = input("Enter key you want to check : ")
    res = search_key(result,key)
    print(res)
    
    
main()
