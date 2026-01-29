# 객체 지향 프로그래밍의 4가지 핵심 개념이자 특징
# 1. 상속 - 부모 클래스의 속성 or 메소드를 자식 클래스에서 물려받아서 사용
# 2. 추상화 - 복잡한것은 숨기고 단순한 것은 드러냄 (클래스 내 콩통적인(반복적인) 코드는 부모 클래스에 구현하라)
# 3. 다형성 - 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다는 뜻 (메서드 오버라이딩)
# 4. 캡슐화 - 객체의 일부 구현 내용에 대해 외부로부터 엑세스 차단 (접근차단)

class Plus_minus():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def plus(self):
        result = self.first + self.second
        return result
    
    def minus(self):
        result = self.first - self.second
        return result

class Morefunction(Plus_minus):  # 상속해줄 클래스명 
    def __init__(self, first, second, third):
        # 생성자 함수 안에서의 super()는 부모 클래스의 init을 받겠다
        super().__init__(first, second)
        self.third = third

    def mul(self):
        result = self.first * self.second * self.third
        return result
    
    def plus(self):
        result = self.first + self.second + self.third
        if result > 100:
            print('버그')
        else:print(result)
        return result

    def parents_plus(self):
        # 부모 클래스의 함수 불러오기
        ret = super().plus()
        return ret

b = Morefunction(3,4,5)

print(b.mul()) # 60
print(b.plus()) # 12
c = Morefunction(1,1,100)
c.plus()
t = Morefunction(300,500,200)   
print(t.parents_plus())         # 800


# 상속관계 확인용 
print(Morefunction.mro()) 
# [<class '__main__.Morefunction'>, <class '__main__.Plus_minus'>, <class 'object'>]


# --------------------------------------
# 다형성 : 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다.
# 다형성을 대표하는 것이 메서드 오버라이딩 

# 메서드 오버로딩 (파이썬에서 지원하지 않음) 


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    def __init__(self, name):
        self.name = name + '츄피'
    
    
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')  
print(baby1.name)
print(FirstChild.mro())  # [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]
print(baby1.cry())  
print(baby1.swim())
print(baby1.walk())
print(baby1.gene) 


# 1. public : 외부에서 값 바꿀수 잇음 (외부로부터 모든 접근을 허용)
class Person():
    def __init__(self, name,age):
        self.name = name
        self._age = age
    def getage(self):
        return self._age

# 2. protected : 자기자신 클래스 내부 또는 자식클래스에서만 접근을 허용
class Person():
    def __init__(self, name,age):
        self.name = name
        # age를 protected처리 하려면 _를 앞에 넣기 => 강제성 없음
        self.age = age
    def getage(self):
        return self.age
    
class Child(Person):
    def print_age(self):
        print(f'자식 클래스에서 접근 : {self.age}')

p = Child('이송미', 22)
p.print_age()       # 자식 클래스에서 접근 : 22


# 속성 이름 앞에 _ 가 있다면 클래스 외부에서 변경하지 말자는 개발자들만의 약속이지 강제성은 없음
p._age = 26         # 강제성이 없어서 출력이 됨
                    # 외부에서 접근해도 값은 변경됨
print(p._age)       



# 3. private : 외부에서 값 바꿀 수 없어

class Person():
    def __init__(self, name,age):
        self.name = name
        # age를 private처리 하려면 __를 앞에 넣기
        self.__age = age


p2 = Person('윤수영', 20)
print(p2.name)
# print(p2.__age)       # AttributeError: 'Person' object has no attribute '__age'


# 외부에서 읽기는 가능하게 하고 싶다면? @property   getter
# 외부에서 쓰기도 가능하게 하고 싶다면? @setter
# 이때 사용하는 decorator
# @property   @setter
class Person():
    def __init__(self, name,age):
        self.name = name
        # age를 private처리 하려면 __를 앞에 넣기
        self.__age = age

    # 오버로딩처럼 보이지만 데코레이터 때문에 서로 다른 함수로 인식해 다르게 작동함.
    @property       # getter 함수의 데코레이터는 property이고, 비공개 속성의 값을 읽는 용도로 사용한다
    def age(self):
        return self.__age
    
    # setter를 쓰려면 getter가 무조건 있어야함
    @age.setter
    def age(self, value):
        self.__age = value
        

p1 = Person('수3영', 40)
print(p1.name)
# print(p1.__age)
# print(p1.age)       # getter함수는 괄호를 생략 가능함

p1.age = 99         # setter 함수 접근
print(p1.age)       # getter로 age 읽기

