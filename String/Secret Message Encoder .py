'''
Question 1: Secret Message Encoder

*Scenario:*  
You are a spy tasked with encoding secret messages. The encoding involves replacing each letter in the message with the letter that is two positions forward in the alphabet. For example, 'a' becomes 'c', 'z' becomes 'b'. Spaces and punctuation should remain unchanged.

*Sample Input/Output:*

1. Input: "hello world"  
   Output: "jgnnq yqtnf"

2. Input: "spy"  
   Output: "uq{

3. Input: "zebra!"  
   Output: "bgdct!"

4. Input: "python 3.8"  
   Output: "rwdqpk 3.8"

5. Input: "a b c"  
   Output: "c d e"
'''


str = input()
encrpyt = ""
for i in  range(len(str)):
    if str[i].isalpha():
        encrpyt += chr(ord(str[i]) + 2 )
    else :
        encrpyt += str[i]
print(encrpyt)
