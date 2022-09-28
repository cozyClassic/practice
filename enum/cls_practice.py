class Person:
    def __init__(self, age):
        self.age = age

    @classmethod
    def is_animal(cls):
        return True
    
    def get_age(self):
        return self.age

    
    
p = Person(20)

print(p.get_age())
print(p.is_animal())
print(Person.is_animal())