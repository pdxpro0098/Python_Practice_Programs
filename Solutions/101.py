# Krish's Approach
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


c = Circle(12)
area = c.area()
print(area)

# Dalip's Approach
class circle:
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius * self.radius
    

c1 = circle(8)

area = c1.area()
print(area)
