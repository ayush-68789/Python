def prime (num):
    count = 0
    for i in range(2,num):
        if (num % i == 0):
            count += 1 
    if count > 0:
        print(num," not prime")
    else:
        print(num," prime")
            
n = input()
total = 0 
for i in n :
    total += int(i)
prime(total)
