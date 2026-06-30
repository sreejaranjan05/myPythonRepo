a = float(input("Enter your marks in English out of 100"))
b = float(input("Enter your marks in Maths out of 100"))
c = float(input("Enter your maths in Computer Science out of 100"))

per = ((a+b+c)/300)*100

if per>=90:
    print("A1")
elif (per>=80 and per<90):
    print("A2")
elif (per>=70 and per<80):
    print("B1")
elif (per>=60 and per<70):
    print("B2")
elif (per>=50 and per<60):
    print("C1")
elif (per>=40 and per<50):
    print("D")
else:
    print("E")
