class myClass():
    def __init__(self, name,age):
        self.name = name
        self.age = age

cls = myClass("krish",20)

print(cls.__dict__)