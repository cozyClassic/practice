from enum import Enum, auto


# IntEnum에는 int만 값이 적용 가능하다.
class MyEnum(Enum):
    Green = 1


# Enum을 호출하는 방법

print(MyEnum.Green)
# MyEnum.Green

print(MyEnum(1))
# MyEnum.Green


# 멤버(키)가 중복될 수 없음
# TypeError: Attempted to reuse key: 'Green'
class DupliacateError(Enum):
    Green = 1
    # Green = 2

# Enum의 값으로 auto()를 사용할 수 있음.
class MyColor(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(list(MyColor))
# [<MyColor.RED: 1>, <MyColor.GREEN: 2>, <MyColor.BLUE: 3>]

# Enum에 대해 For문도 돌릴 수 있음.
for color in MyColor:
    print(color)
# MyColor.RED
# MyColor.GREEN
# MyColor.BLUE

# Enum 안에 뭐가 있는지 확인하는 법
print(hasattr(MyColor,"GREEN"))
# True
print(hasattr(MyColor,"BLACK"))
# False

