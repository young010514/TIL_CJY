# 메소드 종류
# 1. 인스턴스 메소드
#       인스턴스 속성 값에 변화를 준다

# ===============================
# 아래의 두 메소드는 인스턴스 값을 직접적으로 바꾸지 않는다
# 데코레이터를 이용해서 소스 코드를 작성

# 2. 정적 메소드 (static)
# 3. 


# ======================
# decorator : 함수가 다른 함수의 인자값으로 사용이 가능
# 함수 안에서 또 다른 함수를 만들어서 리턴할 수 있다

def deco(func):
    def wrapping(value):
        print("우유"*3)
        func(value)
        print("aza"*3)
    return wrapping

@deco
def call_name(name):
    print(name)

@deco
def call_age(age):
    print(age)

call_name("최민호")
call_age(42)

# 정적 메소드
class Car:
    def __init__(self, name,price):
        self.name = name
        self.price = price
    
    # self라는 매개변수 필요 없음
    @staticmethod
    def add_price(one,another):
        print(one + another)

kia = Car("k8", 300)
bmw = Car("m8", 500)

Car.add_price(500, 700)

# ** 데코레이터가 필요한 이유 : 
#           추후 큰 규모의 프로젝트에서 가독성을 위해 데코레이터를 추가
#           굳이 없어도 되지만, 있으면 나중에 있을 유지보수를 위해 추가하는 것을 추천

# 1. 데코레이터 사용 2. self 없음 3. 클래스 단위로 접근
# 인스턴스 속성 값을 직접 영향을 끼치지 않는 함수다 ~~ 라는 것을 알려주는 역할
# static method == 인스턴스의 속성값을 바꾸지 않는 코드



# ==========================
# 3. 클래스 메소드 Class method
class Make_pies:
    cnt = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Make_pies.cnt += 1
    
    @classmethod        # 클래스 메소드는 클래스 변수를 변경하고 싶을때 접근하는 함수이다
    def number_Of_Pies(cls):    # cls == class
        print(f"파이를 {cls.cnt}명이 만들고 있습니다")

    @classmethod
    def from_birthday(cls, name, birth_year):
        age = 2026-birth_year
        return cls(name,age)
    


a = Make_pies('kevin', 30)
b = Make_pies('java', 22)

# 생성자 함수 대신 클래스메소드로 접근해 객체 생성하기
c = Make_pies.from_birthday('jajd', 1990)
print(c.age, c.name)


Make_pies.number_Of_Pies()  
# a.number_Of_Pies()        # 클래스 변수는 객체로 접근하지 말것!

# 1. 데코레이터 사용 2. 매개변수는 cls (class) 3.클래스 단위에서 호출할것

# *** 클래스 메소드는 생성자 함수를 대체해서 만들기도 함
