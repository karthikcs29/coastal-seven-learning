class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student("Prudhvi", 21)
s2 = Student("Teja", 22)

s1.show()
s2.show()