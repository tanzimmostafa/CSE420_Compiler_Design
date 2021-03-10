import re
file = open('input.txt', 'r')

file_as_list=file.readlines()# each line becomes a list element
#print(file_as_list)

characterlist=[]
for i in file_as_list:#for every line
    temp=i.split()#list of characters
    for j in temp:
        characterlist.append(j)
        
#print(characterlist)    


keywords=[]
identifiers=[]
mathop=[]
logicalop=[]
numericalval=[]
others=[]

keywordmatch=['if','else','elif','for','while','int','float','continue',
              'in','and' ,'def', 'finally' ,'not','or','break','switch',
              'case','void','do']
  
mathopmatch=['=', '+', '-', '*', '/', '%', '++', '--']
logicalopmatch=['==', '!=', '>', '>=', '<', '<=', '&&', '||', '!']
othersmatch= [',', ';', '(', ')', '{', '}', '[', ']']     
numericalregex="^(\d*\.)?\d+$"
identifiersregex="[a-zA-Z]+[a-zA-Z0-9_$]*"


for i in characterlist:
    if i in keywordmatch and i not in keywords:
        keywords.append(i)
    
    temp1=i.strip( ';,]}[{)(' )#removing any ,;    
    if re.search(identifiersregex,temp1):
        if temp1 not in identifiers and temp1 not in keywordmatch:
            identifiers.append(temp1)
    
    if i in mathopmatch and i not in mathop:
        mathop.append(i)
        
    if i in logicalopmatch and i not in logicalop:
        logicalop.append(i)
        
    temp2=i.strip( ';,]}{[)(' )#removing any ,;
    if re.search(numericalregex,temp2) :
         if temp2 not in numericalval:
             numericalval.append(temp2)
             
    for x in othersmatch:#looping each string of characters
         #i may contain 2 characters
         if x in i and x not in others:#x in i is comparing 2 strings
            others.append(x)
            
print("Keywords: ", end=' ')#white space at end instead of newline
print(*keywords, sep=", ")#print all keywords comma separated
print("Identifiers: ", end=' ')
print(*identifiers, sep=', ')
print("Math Operators: ", end=" ")
print( *mathop, sep = ", " )
print("Logical Operators: ", end=" ")
print( *logicalop, sep = ", " )
print("Numerical Values: ", end=" ")
print( *numericalval, sep = ", " )
print("Others: ", end=" ")
print( *others)















     
        
        