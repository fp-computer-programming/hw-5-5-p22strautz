# Author: SCT (AMDG) 11/2/21

string = input("Enter a string to be cut:\n")

length = len(string)

half = length // 2

print(string[0:half])

print(string[half:length])
