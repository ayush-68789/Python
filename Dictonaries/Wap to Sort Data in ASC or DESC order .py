_dict = eval(input())
order = input()
if order == 'asc' :
    res = dict(sorted(_dict.items(), key = lambda item : item [1]))
    print(res)
elif order == 'desc' :
    res = dict(sorted(_dict.items() , key = lambda item : item[1], reverse = True))
    print(res)


'''
Terminal : 

{'a' : 2 , 'b' : 1 , 'c' : 3 }
asc 
{'b': 1, 'a': 2, 'c': 3}



{'a' : 2 , 'b' : 1 , 'c' : 3 }
desc
{'c': 3, 'a': 2, 'b': 1}


'''
