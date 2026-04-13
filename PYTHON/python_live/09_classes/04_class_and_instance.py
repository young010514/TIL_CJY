class Singer:
    pass


iu = Singer()
bts = Singer()

print(type(iu))
print(type(bts)) # <class '__main__.Singer'>

# 문자열 변수 name 은 (정확히는 'Alice')는 str 클래스의 인스턴스
name = 'Alice'
print(type(name)) # <class 'str'>

data =[1,2,3]
print(type(data)) # <class 'list'>

# 데이터들이 메서드를 호출할 수 있었던 이유
# 문자열 name이 사용할 수 있는 메서드인 split()는 클래스 str에 정의되어있음
# 리스트 data가 사용할 수 있는 메서드인 append()는 클래스 list에 정의되어있음
