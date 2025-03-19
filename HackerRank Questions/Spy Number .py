'''Write a program to check if a given number is a Spy number. A Spy number is a number where the sum of its digits is equal to the product of its digits.
Input Format
An integer 𝑥 is provided as input.
Constraints
1 ≤ 𝑥 ≤ 10^6
Output Format
Print "Spy Number."if the given number is a Spy number. Otherwise, print "Not a Spy Number."
Sample Input 0
1124
Sample Output 0
Spy Number
Sample Input 1
14125
Sample Output 1
Not a Spy Number'''

n = int(input())
str = str(n)
sum = 0 
prod = 1 
for i in range(0,len(str)):
    sum += int(str[i])
    prod *= int(str[i])
    
if sum == prod:
    print("Spy Number")
else :
    print("Not a Spy Number")
