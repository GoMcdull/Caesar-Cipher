def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele  
    return str1  
def Testallcases(textlist):
    for a in range(26):
        uppershiftedlist=[]
        shiftedlist=[]
        result=[]
        for i in range(26):
            shiftedlist.append(originlist[(i+a)%26])
            uppershiftedlist.append(upperoriginlist[(i+a)%26])
        for i in range(len(textlist)):
            stored=str(textlist[i])
            if stored.isupper()==True:
                result.append(upperoriginlist[uppershiftedlist.index(textlist[i])])
            elif stored.islower()==True:
                result.append(originlist[shiftedlist.index(textlist[i])])
            else:
                result.append(stored)
        if listToString(result)!=text:
             print("Test"+str(a)+": (shift="+str(a)+"): "+listToString(result))

origin="abcdefghijklmnopqrstuvwxyz"
originlist=list(origin)
upperorigin="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upperoriginlist=list(upperorigin)
uppershiftedlist=[]
shiftedlist=[]
result=[]

type=int(input("Enter 1 for encryption, 2 for decryption: "))
if type==1:
    text=input("Enter your text: ")
    textlist=list(text)
    shift=int(input("Enter the shift: "))%26
    for i in range(26):
        shiftedlist.append(originlist[(i+shift)%26])
        uppershiftedlist.append(upperoriginlist[(i+shift)%26])
    
    for i in range(len(textlist)):
        stored=str(textlist[i])
        if stored.isupper()==True:
            result.append(uppershiftedlist[upperoriginlist.index(textlist[i])])
        elif stored.islower()==True:
            result.append(shiftedlist[originlist.index(textlist[i])])
        else:
            result.append(stored)
    print("Encrypted text: "+listToString(result))
    
elif type==2:
    text=input("Enter encryted text: ")
    textlist=list(text)
    shift=int(input("Enter the key or Enter -1 to perform a Brute Force Attack: "))
    if shift==-1:
        Testallcases(textlist)
    else:
        for i in range(26):
            shiftedlist.append(originlist[(i+shift)%26])
            uppershiftedlist.append(upperoriginlist[(i+shift)%26])
        for i in range(len(textlist)):
            stored=str(textlist[i])
            if stored.isupper()==True:
                result.append(upperoriginlist[uppershiftedlist.index(textlist[i])])
            elif stored.islower()==True:
                result.append(originlist[shiftedlist.index(textlist[i])])
            else:
                result.append(stored)
        print("Decrypted text: "+listToString(result))
else:
    print("Invalid choice")