
'''*Scenario:*  
You are creating a word game where players need to find anagrams of a given word. Write a function that checks if two strings are anagrams of each other (i.e., they contain the same characters in a different order, ignoring spaces and case).

*Sample Input/Output:*

1. Input: "listen", "silent"  
   Output: True

2. Input: "triangle", "integral"  
   Output: True

3. Input: "apple", "pale"  
   Output: False

4. Input: "Dormitory", "Dirty room"  
   Output: True

5. Input: "Schoolmaster", "The classroom"  
   Output: True

'''

def anagram(str1 , str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")
    if (sorted(str1) == sorted(str2)):
        print("TRUE")
    else :
        print("FALSE")


str1 = input()
str2 = input()
anagram(str1,str2)
