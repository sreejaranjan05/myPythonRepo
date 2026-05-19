def countline():
    F=open("intro.txt","r")
    D=F.readline()
    c=0
    for i in D:
        if i[0]"A":
            c=c+1
            print(i)
    print(c)
    F.close()
countline()
        

            
