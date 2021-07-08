"""
The whole input must be given at once, like:

2
ab*c*d
a*b(cd)+e?f
3
acccd
abbbbbcccc
bcdcdef

"""

import re

temp= input("Enter entire input at once: ")  

tlist= temp.splitlines() #input turned into list with each line as a list item

pattern = [] #pattern list
matcher = [] #matcher list

a = int(tlist[0])     #gives number of patterns or regex
b =int(tlist[a + 1])  #gives number of matchers


for i in range(a):
    pattern.append(tlist[i+1])

#print(pattern)

for j in range(b):
    matcher.append(tlist[a+j+2])

#print(matcher)

#Here the output is generated through matching
for i in matcher:
    
    flag = 0
    for j in pattern:
        p = re.compile(r'{}'.format(j)) #p refers tothe pattern
       
        result = re.match(p, i)
        if result:
            print("YES,", pattern.index(j)+1)
            flag = 1
                       
    if flag == 0:
        print("No,",0)
            