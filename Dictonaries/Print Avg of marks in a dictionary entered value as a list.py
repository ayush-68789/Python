dict = eval(input())
name = input()
avg = 0 
if name in dict :
    marks  = dict[name]
    avg = sum(marks)/ len(marks)
    print("%0.2f" % avg)



"""
Terminal : 

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

o/p : 56.00
