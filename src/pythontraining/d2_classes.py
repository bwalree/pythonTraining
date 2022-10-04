from datetime import date

class Person:
    def __init__(self, name, age, birth_date):
        self.name = name
        self.age = age
        self.birth_date

    def say_hello(self):
        print(f"{self.name} says hello")

    def calc_age(self):
        today = date.today()
        birth_year = date. datetime. strptime(birth_date, "%Y-%m-%d)
        age = today.year - birth_year
        return age


p1 = Person("John", 42)
print(p1.name)
print(p1.age)

p2 = Person("Jane", 42)
p2.say_hello()


class Student(Person):

    def learn(self, language):
        print(f"{self.name} is learning {language}")

s1 = Student('John', 42)
s1.say_hello()
s1.learn('Java')




