'''Input Format: A string s consisting of English alphabets, both uppercase and lowercase.
Output Format: Return the encrypted string after applying the custom encryption rules.
Example
Input Hello
Output Fgjnm
Explanation 
For characters at odd positions, the ASCII value of the character is decreased by 2. For characters at even positions, the ASCII value of the character is increased by 2

'''

str = input()
encrypt = []
for i in range(len(str)):
    char = str[i]
    if(i + 1) % 2 == 1 :
        encrypt += chr(ord(char) - 2 )
    else : 
        encrypt += chr(ord(char) + 2 )
print(encrypt)
