# Krish's Approach
class Calculator:
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y


print(Calculator.add(10, 2))
print(Calculator.sub(10, 2))
print(Calculator.mul(10, 2))
print(Calculator.div(10, 2))


# Dalip's Approach
class Calculator:
    
    def add(a,b):
        return a + b

    def subtract(a,b):
        return a - b

    def product(a,b):
        return a * b

    def divide(a,b):
        if(b == 0):
            return "Error! Division by zero."
        return a / b


print("Addition:",Calculator.add(3,5))
