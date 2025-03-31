'''
TERMINAL : 
Enter entry : 5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''


def square_dict (entry) :
    data = {}
    for i in range(1,entry+1):
        data[i] = i*i
    return data

entry = int(input("Enter entry : "))
result = square_dict(entry)
print(result)
