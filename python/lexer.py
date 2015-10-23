exp = 'if(a==b)\n\tprint("hello")'
buff = ""
alpha = [chr(i) for i in range(97,123)]
i=0
while(i!=len(exp)-1):
    buf+=exp[i]
    if buf in alpha and exp[i+1] in alpha:
        j=i
        while(exp[j] in alpha):
            buf+=exp[j]
            j+=1
        i=j
    elif:
        
