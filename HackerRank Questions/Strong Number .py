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


def fact (num):
    fac = 1 
    for i in range (1,num+1):
        fac *= i
    return fac 

n = input()
sum = 0 
for i in range(0,len(n)):
    sum += fact(int(n[i]))
if (sum == int(n)):
    print("Strong number")
else :
    print("Not strong number")
