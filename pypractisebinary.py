import pickle
def delete():
    F=open("M.dat","rb")
    n=int(input("enter ID your tryna remove"))
    L=[]
    try:
        while True:
            D=pickle.load(F)
            for i in D:
                if D[0]==n:
                    continue
                else:
                    L.append(D)
    except EOFError:
        F.close()
    F=open("M.dat","wb")
    for i in L:
        pickle.dump(i,F)
    F.close()
                    
    

        
