class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

person = Person("John", "Doe", 5)

# 에러 발생 X
print(person._age)
person._age = -1
print(person._age)

# 에러 발생
person = Person("John", "Doe", 5)
print(person.age)
person.age = -1
print(person.age)