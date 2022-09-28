"""
- __init__ 메소드
    - 객체가 생성되어, 초기화되는 순간 '호출'된다.
    - 그러나 객체에 메모리를 할당하지는 않는다.

- __new__ 메소드
    - __init__이 실행되기 전에, 항상 __new__가 먼저 실행된다.
    - 이 때 객체에 메모리가 할당된다.
"""

class Person:
    def __new__(cls,*args,**kwargs):
        super().__new__()
        print(args)
        print(kwargs)
        return
    
    def __init__(self,name,*args,**kwargs):
        print("INIT", args)
        print("INIT", kwargs)
        self.name = name

p = Person("Lee",20,"Seoul", country="Korea", region="Asia")
# ('Lee', 20, 'Seoul')
# {'country': 'Korea', 'region': 'Asia'}
# __init__은 작동하지 않는다. 리턴할 때 cls의 인스턴스를 돌려주지 않았기 때문

print(p)
# None
# Person 객체가 메모리에 할당되지 않으니
# p가 아무런 메모리를 찾지 못하게 된다.

# 따라서 이런 attr에 대한 상호작용도 불가능하게 된다.
print(p.name)
# error

