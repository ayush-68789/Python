'''
The Text Editor
Scenario: You're creating a simple text editor. The editor allows users to input text and perform basic editing operations.

Questions:

Word Count: Write a Python function word_count(text) that takes a text as input and returns the total number of words in the text.

Input: text = "hello world this is a sample text"
Output: 7
Input: text = "the quick brown fox jumps over the lazy dog"
Output: 9
Input: text = "programming is fun"
Output: 3
'''

str = input()
word = str.split()
print(len(word))
