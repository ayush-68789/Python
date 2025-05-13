str = input()
str = str.replace(" ","")
for char in set(str) :
    count = 0 
    for c in str :
        if c == char :
            count += 1
    print(f"'{char}':{count}",end=" ")



# OR USING DICTONARY 

str = input()
str = str.replace(" ","")
freq = {}
for char in str :
    if char in freq :
        freq[char] += 1 
        
    else :
        freq[char] = 1 
print(freq)
