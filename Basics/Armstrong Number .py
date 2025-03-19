n = int(input())
str = str(n)
length = len(str)
sum = 0 
for i in range(0,length):
    sum += int(str[i]) ** length
if (sum == n):
    print("YES")
else:
    print("NO")
