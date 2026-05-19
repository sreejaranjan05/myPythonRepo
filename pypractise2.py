import pickle
def add():
    F=open("C.dat","ab")
    a=input("Enter book to be added")
    b=int(input("Enter book id"))
    c=input("Enter author name")
    L=[a,b,c]
    pickle.dump(L,F)
    F.close()

def search():
    F=open("C.dat","rb")
    s=input("Enter name of book you want to view details of")
    found=False
    try:
        while True:
            D=pickle.load(F)
            if D[0]==s:
                print(D)
                found=True
    except EOFError:
        F.close()
def show():
    F=open("C.dat","rb")
    try:
        while True:
            D=pickle.load(F)
            print(D)

    except EOFError:
        F.close()

z=int(input("Enter one of the following options 1. Add book, 2. Search book, 3. display book"))
if z==1:
    add()
elif z==2:
    search()
elif z==3:
    show()
else:
    print("Envalid option")
    

                
