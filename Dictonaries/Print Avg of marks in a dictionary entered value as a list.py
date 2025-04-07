def user(entries) :
    data = {}
    for i in range(0,entries):
        line = input().split()
        key = line[0]
        value = list(map(float,line[1:]))
        data[key] = value
    return data 
    
    
def main():
    entries = int(input())
    result  = user(entries)
    name = input()
    if name in result :
        marks = result[name]
        avg = sum(marks) / len(marks)
        print("%.2f" % avg)

main()


"""
Terminal : 

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

o/p : 56.00
