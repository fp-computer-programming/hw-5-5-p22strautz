# Author: SCT (AMDG) 11/2/21

word = input("Enter a 6 letter word\n")


odd = ""
even = ""
for i in range(0, len(word)):
    
    if i == 0 or i == 2 or i == 4:
       
        odd = odd+word[i]
        if i != 4:
            odd = odd+'-'
        
    else:
       
        even = even+word[i]
        if i != 5:
            even = even+'-'
        
print(even+'\n')
print(odd+'\n')
