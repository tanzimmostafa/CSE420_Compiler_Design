import re

inputs = []
file= open('input.txt', 'r')
inputs = file.readlines()#turns each line in file as a list item


returntype_l = ['char','void','byte','short','long','int','boolean','float','double']

def func(lw):
    return [char for char in lw]

def returnTypeFunc(x):
    
    for i in returntype_l:
        a = x.find(i)
        if a >-1:
            return i
    
methods=[]#methods list
for i in inputs:
    words = i.split() #words is a list
    lw = words[len(words)-1]
    chars = func(lw)
    
    if chars[len(chars)-1] == ')' or ((chars[len(chars)-1]=='{') and chars[len(chars)-2]==')'):
        methods.append(i)

print("Methods:")
for j in methods:
    text = j    
    returntype = returnTypeFunc(text)
    a = re.search(r"\b(?!main\b)\w+\(((char|byte|void|double|float|boolean|long|int|short) \w+, (char|byte|void|double|float|boolean|long|int|short) \w+)*\)*", text)
    if a != None:
        print(a.group(0) + ", return type: "+ returntype)