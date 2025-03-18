'''
*Scenario:*  
You are developing a text analysis tool that needs to check if a given string is a palindrome. A palindrome reads the same forward and backward, ignoring spaces, punctuation, and case sensitivity.

*Sample Input/Output:*

1. Input: "A man, a plan, a canal: Panama"  
   Output: True

2. Input: "race a car"  
   Output: False

3. Input: "No 'x' in Nixon"  
   Output: True

4. Input: "Was it a car or a cat I saw?"  
   Output: True

5. Input: "hello"  
   Output: False
'''

str = input()
new_str = "" 
for i in range (len(str)):
    if str[i].isalpha() :
        new_str += str[i].lower()
pal_str = new_str[::-1]

if pal_str == new_str :
    print("TRUE")
else :
    print("FALSE")
