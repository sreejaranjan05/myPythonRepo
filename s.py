N=int(input("Enter the number of elements"))
num=[]
for i in range(N):
    n=int(input("enter a number"))
    num.append(n)
if num[0]>num[1]:
    m,m2=num[0],num[1]
else:
    m,m2=num[1],num[0]
# 2,4,6,1,3
for i in num[2:]:
    if i>m2:
        if i>m:
           m,m2=i,m
        else:
            m2=i
print("the second largest number you entered is:",m2)
        

     
