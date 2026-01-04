# Krish's Approach
class myClass():
    def __init__(self, name,age):
        self.name = name
        self.age = age

cls = myClass("krish",20)

print(cls.__dict__)

# Dalip's Approach
class Student:
    def __init__(self,name,roll_no,):
        self.name = name
        self.roll_no = roll_no

s1 = Student("DalipKumar",456)

print(f"Name: {s1.name}")
print(f"Roll No: {s1.roll_no}")
