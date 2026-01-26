# 문자열 관련 함수

st = "apple,banana,mango"


# 1 .find() 메소드
# 내가 원하는 알파벳이 어디에 있는지
index = st.find('a')
print(index) # 0

# 특정 인덱스 이후부터 문자열을 찾고싶다면 
index = st.find('a', 1)
print(index) # 7

# 없는 값 찾을 시 -1 리턴
index = st.find('x') 
print(index) # -1


# 2 .index() 메소드
alpha = st.index('p')  
# alpha = st.index('z') 없는 값을 찾을 시 ValueError  
print(alpha)  # 1

# 내가 원하는 알파벳이 몇개 있는지
print(st.count('a')) # 5

# 대문자 여부
print(st.isupper()) # False
print(st.islower()) # True  ==> ,는 무시하고 전부 소문자인지만 확인함
print(st.isalpha()) # False ==> , 가 isalpha 에 False


# 문자열 관련 함수
st = ['a','p','p','l','e']

# 리스트 안에 ㅣㅇㅆ는 문자열을 하나로 합치기
# join을 이용함
str2 = ' '.join(st)   # 구분자.join(list)
print(str2)

# 리스트 안의 문자를 합치는데, 사이사이에 ,를 넣어주세요
st = ['apple', 'banana','mango']
str2 = ','.join(st)
print(str2)

st = 'apple,banana,mango'
str2 = st.upper()
print(str2)

st = ' apple'
print(st)
str2 = st.lstrip()  # 왼쪽 공백 제거
print(str2)

# 문자열 뒤집기 (reversed 연습)
st = 'apple'
str2 = reversed(st) # reversed 객체 출력 => list변경 => join 활용
print(''.join(list(reversed(st))))
print(st[::-1])  # 이렇게 쓰자

# ============================
# 리스트 관련 함수 / 메서드

# 리스트에 값 추가하기
st = ['apple','banana','mango']
# 'orange'를 추가하기
st.append('orange') # 리스트 맨 뒤에 하나 추가됨
print(st)

# insert 함수 사용 해서
st.insert(1, 'orange') # 1번 index에 orange를 추가!
print(st)

a = st.index('banana')  # index 사용 가능? ==> list 에는 find 메서드가 없음
print(a)

