import functools


@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print('inside str')
        return f"Person: {self.name}, Age: {self.age}"

    def __repr__(self):
        print('inside repr')
        return f"Person: {self.name}, Age: {self.age}"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


person1 = Person("Yuriy", 30)
person2 = Person("John", 30)

# d = dir(person)
# print(d)
# #print(person)
print(person1 >= person2)
