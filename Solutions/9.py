import math

# Quadratic Equation: x^2 + 5x + 6 = 0

# Coffecients of The Quadratic Equation: x^2 + bx + c = 0
a = 1  # Coefficient of x^2
b = 5  # Coefficient of x
c = 6  # Constant term

# Discriminant
d = (b**2) - (4 * a * c)  # Output: 1

# if d > 0 That means we'll get two roots
# else d < 0 That means we'll get two complex roots

if d >= 0:
    root1 = int(-b + math.sqrt(d)) // (2 * a)
    root2 = int(-b - math.sqrt(d)) // (2 * a)
    print("The roots are real:")
    print("Root 1:",root1)
    print("Root 2:",root2)
else: 
    print("The equation has complex roots")
