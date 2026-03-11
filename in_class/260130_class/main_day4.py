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

# extend
st = [1,2,3]
str2 = [4,5]

# st.extend(str2)  
st += str2 # 위와 동일한 방식
print(st)

# 리스트 원소 삭제
st = [1,2,3,4,5]
value = st.pop()   # 마지막 원소 삭제하고, 삭제된 원소를 반환
print(st) # [1,2,3,4]
print(value) # 5

value = st.remove(4)  # 반환값 없음  / 4라는 값을 맨 앞 "하나만" 삭제
print(st) # [1,2,3]
print(value) # None

# 여러개 값을 삭제하고 싶을때
st = [1,2,3,4,5,6]
del st[2:] # slicing을 이용해서 여러 값 삭제
print(st) # [1,2]

# list 뒤집기
st.reverse()
print(st)

st = st[::-1]
print(st)

# 정렬 방법 2가지 (sort/sorted)
a1 = [6,3,9]
print(a1)  # [6,3,9] 
a1.sort()  # 원본 데이터가 정렬이 됨, 반환값 없음
print(a1)  # [3,6,9] 

a1 = [6,3,9]
ret = sorted(a1)   # 원본 데이터 보호(유지), 반환값이 정렬됨
print(ret) # [3,6,9]


# sorted key도 활용
lst = list(range(1, 11))

ret = sorted(lst, key = lambda x: -x)   # 리스트 내의 값이 정수일때만  사용가능
print(ret) # [10,9,8,7,6,5,4,3,2,1]

lst = ['apple','mango', 'banana']
# ret = sorted(lst, key = lambda x: -x)   # 문자열에 -를 붙이는건 error
ret = sorted(lst, reverse=True)
print(ret) # [10,9,8,7,6,5,4,3,2,1]

# 문제
lst = [(3, 'banana'), (2,"apple"), (1,"carrot")]
# 정렬시 조건 / 문자열 기준으로 내림차순
ret = sorted(lst, key = lambda x: x[1], reverse=True)
print(ret) # [10,9,8,7,6,5,4,3,2,1]




# 리스트 copy하기

# 1. 할당 (aggigment) (주소값 복사)
lst=[1,2,3]
lst2=lst
lst[0]=100
print(lst2)

# 2. 얕은복사 (문제 없음)
lst=[1,2,3]
lst2=lst[:]
lst[0]=100
print(lst2)

# 3. 얕은복사 (2차원 리스트 문제 발생)
lst=[[1,2],[3,4]]
lst2=lst[:]
lst[0][0]=100
print(lst2[0][0])

# 4. 깊은복사
import copy
lst=[[1,2],[3,4]]
lst2=copy.deepcopy(lst)
lst[0][0]=100
print(lst2[0][0])

--------------------------------------------------------
 
# # 주소값을 찍어보자 [참고]
# # a=5
# # b=5
# # print(id(a),id(b))
# # a=3
# # print(id(a),id(b))

# # a=5
# # b=a
# # print(id(a),id(b))
# # a=3
# # print(id(a),id(b))

# # lst=[1,2,3]
# # lst2=lst
# # print(id(lst),id(lst2))
# # lst[0]=100
# # print(lst2)
# # print(id(lst),id(lst2))

# # lst=[1,2,3]
# # lst2=lst[:]
# # print(id(lst),id(lst2))
# # lst[0]=100
# # print(lst2)
# # print(id(lst),id(lst2))

# # lst=[[1,2],[3,4]]
# # lst2=lst[:]
# # print(id(lst),id(lst2))
# # print(id(lst[0]),id(lst2[0])) #주소값 같음
# # lst[0][0]=100
# # print(lst2)

# # import copy
# # lst=[[1,2],[3,4]]
# # lst2=copy.deepcopy(lst)
# # print(id(lst[0]),id(lst2[0])) #주소값 다름
# # lst[0][0]=100
# # print(lst2)