class MyClass:
    def method(self):
        return 'instance method', self
    
    @classmethod
    def class_method(cls):
        return 'class method', cls
    
    @staticmethod
    def static_method():
        return 'static method'
    
    @classmethod
    def class_method_args_self(self):
        return 'what is this?', self
        # class를 반환한다. 변수명이 중요한게 아님
    

print(MyClass.static_method())
# static method
print(MyClass.class_method())
# ('class method', <class '__main__.MyClass'>)
# print(MyClass.method()) # 에러

my_instance = MyClass()
print(my_instance.static_method())
# static method
print(my_instance.class_method())
# ('class method', <class '__main__.MyClass'>)
print(my_instance.method())
# ('instance method', <__main__.MyClass object at 0x103166f10>)

print(MyClass.class_method_args_self())