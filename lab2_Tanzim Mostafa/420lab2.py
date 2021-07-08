def checker(addresses):
    count=0    
    for address in addresses:#for each address/input
        count+=1
        temp=list(address)#turns address into a character list
        atcount=temp.count('@')#counts number of @ symbols
        if atcount!=1:# There must be exactly 1 @ symbol to be an email
            
            if '.' not in address or atcount!=0:# There must be atleast 1 '.' in a webaddress
                print('Not an email or web address')
                
            else:
                lastperiod=address.rfind('.')#finds index of last occurrence of '.'
                c=method1(address[:lastperiod])#sending part of string before last '.'
                d=method3(address[(lastperiod+1):])#sending part of string after last '.'
                if c is True and d is True:
                    print("Web,",count)
                else:
                    print("Not an email or web address")            
            
       
        else:
            parts=address.split("@")
            a=method1(parts[0])
            b=method2(parts[1])
            if a is True and b is True:
                print("Email,",count)
            else:
                print("Not an email or web address")
        
def method1(part1):
    charlist=list(part1)#converting string to a character list
    temp1= ord(charlist[0])#contains ascii number
    if ( (temp1>=97 and temp1<=122) or (temp1>=65 and temp1<=90) )==False:
        return False
    else:#if first character is a letter
        for i in range(1,len(charlist)):
            temp2=ord(charlist[i])
            if ( (temp2>=97 and temp2<=122) or (temp2>=65 and temp2<=90) \
                or (temp2>=48 and temp2<=57) or (temp2==46) \
                    or (temp2==45) ) == False:
                return False
            else:
                continue
            
        return True                
                        
def method2(part2):
    if "." not in part2:#atleast 1 '.' symbol hasto be present
        return False
    else:
        lastperiod=part2.rfind('.')#finds index of last occurrence of '.'
        charlist=list(part2)
        
        for i in range(lastperiod):
            temp1=ord(charlist[i])#finds ascii number of character
            if ( (temp1>=97 and temp1<=122) or (temp1>=65 and temp1<=90) \
                or (temp1==46) or (temp1==45) )== False: 
                return False
            else: 
                continue
                        
        for j in range(lastperiod+1,len(charlist)):
            temp2=ord(charlist[j]) #finds ascii number of character           
            if ( (temp2>=97 and temp2<=122) or (temp2>=65 and temp2<=90) )==False:
                return False
            else:
                continue
            
        return True
        
        
def method3(part2):
    #tld=top level domain
    tldlength=len(part2)
    if tldlength>=2 and tldlength<=63:
        charlist=list(part2)
        for i in range(len(charlist)):
            temp=ord(charlist[i])#converting to ascii
            if ( (temp>=97 and temp<=122) or (temp>=65 and temp<=90) )==False:
                return False
            else:
                continue             
    else:
        return False
    
    return True
            
lines=input("Enter a number: ")
addresses=[]

for i in range(int(lines)):
    temp= input("Enter email or web address: ")
    addresses.append(temp)
    
checker(addresses)         
        
        
    
        
