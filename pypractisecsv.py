def upper():
    F=open("A.txt","r")
    D=F.read()
    W=D.split()
    for i in W:
        if i[0].isupper() == True:
            print(i)
    F.close()
upper()
            
    
    
