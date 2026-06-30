import os
print(os.getcwd())

import pickle
def search():
    n=input("Enter movie names to be searched")
    F=open("C.dat","rb")
    found=False
    try:
        while True:
            d=pickle.load(F)
            if d[1]==n:
                print(d)
                found=True
    except EOFError:
        F.close()

def show():
    F=open("C.dat","rb")
    try:
        while True:
            d=pickle.load(F)
            print(d)
    except EOFError:
        F.close()

def update():
    F=open("C.dat","rb")
    L=[]
    try:
        while True:
            d=pickle.load(F)
            if d[3].lower()=="karan johar":
                L.append([d[0],d[1],(d[2]*1.1),d[3]])
            else:
                L.append(d)
    except EOFError:
        F.close()
    F=open("C.dat","wb")
    for i in L:
        pickle.dump(i,F)
    F.close()

def delete():
    a=int(input("enter movie ID which is to be deleted"))
    F=open("C.dat","rb")
    L=[]
    try:
        while True:
            d=pickle.load(F)
            if d[0]!=a:
                L.append(d)
    except EOFError:
        F.close()
    F=open("C.dat","wb")
    for i in L:
        pickle.dump(i,F)
    F.close()


            
    
    
   
            
    
