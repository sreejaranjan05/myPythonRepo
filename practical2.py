# Function returning multiple values using a tuple
def calculate(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    return sum_result, difference, product
results = calculate(10, 5)
print(results)  
