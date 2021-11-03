# Author: SCT (AMDG) 11/2/21
word1 = input("Enter a word\n")

word2 = input("Enter a different word\n")

word3 = input("Enter another different word\n")

x = [word1, word2, word3]
x.sort()

for s in x:
    print(s)
    