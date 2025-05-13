dict = eval(input())
new_dict = {}
key = input()
value =int(input())
new_dict[key] = value 

dict.update(new_dict)
print(dict)


'''
Terminal : 
{'a' : 2 , 'b' : 3 }
c
5
{'a': 2, 'b': 3, 'c': 5}

'''
