# class ClassName:
#     code goes here


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}."

    def add_skill(self, skill):
        self.skills.append(skill)


# p = Person("Chenyun","Zhang","26","USA","NYC")
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)
# print(p.person_info())
# p.add_skill("JavaScript")
# print(p.skills)


# note Inheritance
# class Student(Person):
#     pass

# We didn't call the init() constructor in the child class.
# If we didn't call it then we can still access all the properties from the parent.
# But if we do call the constructor we can access the parent properties by calling super.
# We can add a new method to the child or we can overwrite the parent class by creating the same method name in the child class. 
# When we add the init() function, the child class will no longer inherit the parent's init() function.

class Student(Person):
    def __init__(self, firstname, lastname, age, country, city):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return f"{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}."


s1 = Student("Tracy", "Zhang", 18, "China", "Fuzhou")
print(s1.person_info())
s1.add_skill("Python")
print(s1.skills)