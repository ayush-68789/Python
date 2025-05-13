'''
TERMINAL : 
{1 : 'a' , 2:'b'}
{2:'c' , 3 : 'd'}
{1: 'a', 2: 'c', 3: 'd'}


 '''
dict_1 = eval(input())
dict_2 = eval(input())
merge = {}
merge = dict_1.copy()
merge.update(dict_2)
print(merge)
