# Author: SCT (AMDG) 11/2/21

word = input("Enter a word to check for palindrome\n")

if word == word[::-1]:
    print('Forward: ' + word)
    print('Backward: ' + word[::-1])
else:
    print('Forward: ' + word)
    print('Backward: ' + word[::-1])
