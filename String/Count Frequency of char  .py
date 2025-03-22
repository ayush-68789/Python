str = input()
str = str.replace(" ","")
for char in set(str) :
    count = 0 
    for c in str :
        if c == char :
            count += 1
    print(f"'{char}':{count}",end=" ")
