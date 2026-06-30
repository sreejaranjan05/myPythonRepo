import csv
def add():
    f=open("S.csv","a",newline="\n")
    d=csv.writer(f)
    n=int(input("Enter employee number"))
    na=input("Enter employee name")
    j=input("Ennter employee job")
    s=int(input("Enter employee salary"))
    L=[n,na,j,s]
    d.writerow(["eno","ename","job","salary"])
    d.writerow(L)
    f.close()

def display():
    f=open("S.csv","r")
    d=csv.reader(f)
    for i in d:
        print(i)
    f.close()

def head():
    f=open("S.csv","a",newline="\n")
    d=csv.writer(f)
    d.writerow(["eno","ename","job","salary"])
    f.close()

def count():
    f=open("S.csv","r",newline="\n")
    d=csv.reader(f)
    c=0
    next(d)
    for i in d:
        if i[2].lower()=="manager":
            c=c+1
    print(c)
    f.close()

def show():
    f=open("S.csv","r")
    d=csv.reader(f)
    L=[]
    next(d)
    for i in d:
        if int(i[3])<=50000:
            print(i)
    f.close()
    
    
