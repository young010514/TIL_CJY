# 틀 - 클래스
# 클래스 객체 = ㄷ인스턴스 (instance)
# 클래스 내 변수 = 속성 (attribute)
# 클래스 내 함수 = 메소드 (method)

# 객체지향 프로그래밍 방식 : Python, C++, python, go ...
# 절차지향 프로그래밍 방식 : C언어

class Calculator():
    
    numberOfCalcul = 0 # 클래스 변수
    
    def __init__(self): # __로 만드는 함수는 매직메소드 - 생성자 함수(constructor)
        self.result = 0 # 인스턴스 변수
    def getsum(self,value):
        self.result += value
        return self.result
    
cal1 = Calculator()
print(cal1.getsum(3))  # 3
print(cal1.getsum(4))   # 7
print(cal1.result) # 7

cal2 = Calculator()
print(cal2.getsum(6))  # 6
print(cal2.getsum(7))   # 13
print(cal2.result)

# 클래스 변수 변경할땐 인스턴스 말고 클래스로 접근
Calculator.numberOfCalcul = 4 
print(cal1.numberOfCalcul)

# 잘못된 예시 : 클래스 변수를 인스턴스로 접근하면 같은 클래스의 다른 객체들이 서로 다른 값을 내옴
cal1.numberOfCalcul = 10
print(cal1.numberOfCalcul) # 10 
print(cal2.numberOfCalcul) # 4



# ============================
# 메소드 종ㄹ 3가지
# 1. 인스턴스 메소드 (instance method)
# 2. 클래스 메소드 (Class method)
# 3. 정적 메소드 (static method)


# 1. 인스턴스 메소드 (instance method)

# __init__ 이라는 생성자 함수 없이 클래스 만들
class Plus_minus:
    # def data(self, first,second):
    #     self.first = first
    #     self.second = second
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def plus(self):
        result = self.first + self.second
        return result 
    def minus(self):
        result = self.first - self.second
        return result 
    
# a = Plus_minus()
# a.data(3,5)
a = Plus_minus(2,7)

# b = Plus_minus()
# b.data(3,5)
b = Plus_minus(2,7)
print(a.first, b.second)


# __add__ 매직메소드 활용
class Car():
    def __init__(self, name,price):
        self.name = name
        self.price = price
    # + 로 바로 출력하고 싶을떄
    def __add__(self,another):
        return self.price + another.price
    # 인스턴스 변수의 속성은 문장으로 출력하고 싶을 때 자주 사용하는 매직 메소드
    def __str__(self):
        return f'{self.name}의 가격은 {self.price}입니다'
    
kia = Car('k8', 500)
bmw = Car('m5', 300)

print(kia + bmw)    # __add__ 매직 메소드 활용
print(kia)          # __str__ 매직 메소드 활용

# 인스턴스 삭제 del
del kia
del bmw
