import csv
def add():
    f=open("E.csv","w",newline="\n")
    d=csv.writer(f)
    n=int(input("enter no of records"))
    d.writerow(["ENO","ENAME","JOB","SALARY"])
    for i in range(n):
        eno=int(input("enter eno"))
        ename=input("enter name")
        job=input('enter job')
        salary=int(input("enter salary"))
        d.writerow([eno,ename,job,salary])
    f.close()
def display():
    f=open("E.csv","r")
    d=csv.reader(f)
    for i in d:
        print(i)
    f.close()
def count():
    f=open("E.csv","r")
    d=csv.reader(f)
    c=0
    next(d)
    for i in d:
        if i[2].lower()=="fashion designer":
            c=c+1
        else:
            continue
    print("total no of employees with job as fashion designer = ",c)
    f.close()
def show():
    f=open("E.csv","r")
    d=csv.reader(f)
    next(d)
    for i in d:
        if int(i[3])<1000000:
            print(i)
    f.close()

import pickle
def UpdateFare():
    f=open("PASSANGER.DAT","rb")
    L=[]
    try:
        while True:
            d=pickle.load(f)
            for i in d:
                L.append([d[0],d[1],d[2],d[3],d[4]*1.05])
    except EOFError:
        f.close()
        f=open("PASSENGER.DAT","wb")
        pickle.dump(L,f)
        f.close()































    
    
