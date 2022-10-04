class Person:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"My name is {self.name}"

    def __repr__(self):
        return f"Person {self.name}"

    def __gt__(self, other):
        return self.height > other.height


john = Person("John", 20)
print(john)
print(repr(john))

jane = Person("Jane", 10)

print(john > jane)
