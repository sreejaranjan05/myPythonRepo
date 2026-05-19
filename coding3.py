#WAP to input sales made be salesman in 4 quarters. calculate total sales and commission on the basis of following cases:
# >80000 com - 15%
#>60000 and <80000 10%
# >40000 and <60000 8%
#<40000 no commission

q1 = float(input("Enter your total sale in first quater"))
q2 = float(input("Enter your total sale in second quater"))
q3 = float(input("Enter your total sale in third quater"))
q4 = float(input("Enter your total sale in fourth quater"))

sale = q1+q2+q3+q4

if sale>80000:
    print("Your commission is 15% of total sales")
elif (sale>60000 and sale<80000):
    print("Your commission is 10% of total sales")
elif (sale>40000 and sale<60000):
    print("Your commission is 8% of total sales")
else:
    print("no commission")
