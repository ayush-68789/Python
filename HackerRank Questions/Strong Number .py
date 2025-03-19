'''This program checks if a given number is a Strong number. A Strong number is a number in which the sum of the factorials of its digits is equal to the original number.
Input Format Accept an integer 𝑥 from the user.
Constraints 1 ≤ 𝑥 ≤ 10^6
Output Format
Print "Strong Number." if the number is a Strong number
otherwise print "Not a Strong Number.".
Sample Input 0
145
Sample Output 0
Strong Number
Sample Input 1
405
Sample Output 1
Not a Strong Number'''


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
