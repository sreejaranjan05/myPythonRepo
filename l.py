#WAP to delete all odd numbers and negative numbers from
# the given list
L1=[11,-1,22,-3,33,55,44,-50,46,101,77,-100,42]
L=len(L1)
print(L)
for i in range(L):
    if (L1[i]%2==1) and (L1[i]<0):
        L1.remove(L1[i])
print(L1)
