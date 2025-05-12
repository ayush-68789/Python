def prime(num):
    count = 0 
    for i in range(2,n):
        if (num % i == 0):
            count += 1 
    if count == 0 :
        print("Prime")
    else:
        print("NOt Prime")
n = int(input())
sum = 0 
for i in range(0,n+1):
    sum += i
print(sum)
prime(sum)
