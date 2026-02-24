# if 문실습
# n = int(input())
# if n % 2 == 0 : print("짝수")
# else :print("홀수")

# 별 10개 반복 출력
z = 0
while z<10:
    print("*", end=' ')
    z+=1
print()
# for 문
numbers = [1,2,3,4,5,6,7,8,9]
# 이 리스트에서 홀수만 찾아서 그 값을 출력해주세요
# for x in numbers:
#     if x%2 != 0 :print(f"{x}은(는) 홀수입니다")

[print(f"{x}은(는) 홀수입니다") for x in numbers if x%2 !=0]


# 함수?? 자주 사용하는 코드들을 하나로 묶어놓은것 
# 함수 정의 def 함수명 : 
def abc():
    print("   ()   ()   ")
    print("   ( 0  0 )   ")
    print("   (  ㅗ  )   ")
    print("   ()   ()   ")


# 모듈 (함수랑 변수 등 코드를 모아놓은 파일)
#      (누군가가 미리 만들어 놓은 파일을 가져다 사용할 것임)
import random
menu = ['마라탕','요아정','새마을식당']
select_lunch = random.choice(menu)
print(select_lunch)
select_lunch = random.choices(menu, k=2) # 중복됨
print(select_lunch)
select_lunch = random.sample(menu, k=2) # 중복안됨
print(select_lunch)

# swap
y,x = 1, 5
# y = 1, x = 5
# 결과 ==> x = 1, y = 5

# temp = y
# y = x
# x = temp
# print(y, x) # swap 후 ==> 5, 1 출력

# 굳이 이렇게 안하고 
x,y = y,x # 이와 같은 형태로 가능 
print(y, x)

# Boolean
a, b = 0, -1
a, b = bool(a), bool(b)
print(a, b)

# 소숫점
a = 3.14
print(round(a, 1))  # 소수점 1번째
print(f'{a:.1f}')   # 소수점 1번째
a = 3.15
print(f'{a:.1f}')   # 결과 : 3.1 (컴퓨터의 불확실성 3.2가 아닌 3.1로 표현)
# flooting pointer 부동소수점 이라는 것을 이용해서 실수 표현 하는데
# 정확한 표현이 아닌 근사값으로 표현함 

a = 1.2 - 1.1
print(a)  # 0.1을 정확히 표시하지 못하고 근사치를 표현함 ==> 프로그래밍의 한계
print(round(a, 1))
print(round(1.15 + 0.000000001, 1)) # 이와 같이 아주 작은 값을 더해서
print(round(1.15 + 1e-8, 1)) 

# 순서가 있는 자료형
# string, list, tuple, range
s = 'abcdefg'
print(s[:3])    # abc 
print(s[3:])    # defg
print(s[2:5])   # cde
print(s[5:2:-1])  # fed
print(s[1:6:2]) # bdf
print(s[::-1])  # gfedcba
print(s[-2])    # f


# replace
s = 'abcde'
ret = s.replace(s[1], 'k')
print(ret, s)

capital = 'A'
test1 = capital.lower()
print(test1) # 'a'

# ascii code 아스키 코드 값을 이용한 변환
# 컴퓨터는 문자 자체를 저장하지 못하고, 문자를 숫자로 변환한 후에 저장한다.
# 전세계적으로 문자를 전환할 숫자를 통일한 게 아스키코드


# 대문자와 소문자 사이의 아스키코드 값의 차이는 32 ex. 'a' = 97, 'A'=65 

capital = 'A'
print(ord(capital))          # ord() : 문자를 -> 아스키코드값   65 
print(chr(ord(capital)+32))  # chr() : 아스키코드값 -> 문자     a

small = 'b'
test1 = small.upper()   # 내장함수 이용
print(test1)   # B
test2 = chr(ord(small) - 32)     # 아스키코드 이용
print(test2) # B

# 리스트 기초2 
lst = [1,2,3,4]
print(type(lst))
print(len(lst))

# 리스트 연산 
print(lst * 3)
print(lst + [9, 8, 7])

# tuple
# 튜플은 안에 있는 값을 바꿀수 없음 => 불가변성
tp = (1,2,3,4,5)
print(tp)       # (1,2,3,4,5)
print(type(tp)) # tuple
print(tp[1])    # 2
print(len(tp))   # 5


# ===============================
# 순서 개념이 없는 => dictionary, set
 
di={1:3,
    2:{4:5},
    '학':6,
    '교':[7,8,9]
    }
di[2] = 'ddddd'
print(di)

di[111] = di.pop(1)
# .pop(): 리턴값은 없어지는 원소의 value
# 리턴값이 없으면 원본 변환이 되고, 
# 리턴값이 있으면 원본 변환이 없는 것이 일반적이지만 그 예외의 경우가 있음 ex. dict.pop() 

print(di)


# set
# 중복 불가능하며, 순서가 없는 자료구조
s = {1,2,3,4,5,6,3,1,5,1}
print(s, type(s))

lst = [1,2,1,1,212,3,4,2,23,5,2,6,2,2]

s1 = {1,2,3}
s2 = {3,6,9}

# set 합집합 차집합 교집합
# 합집합
print(s1 | s2)  # {1,2,3,6,9}
# 차집합
print(s1 - s2)  # {1,2}
# 교집합
print(s1 & s2)  # {3}


# True False 실습
print('a' and 'b')  # b
print('' and 'a')   # ''
print(0 and 1)      # 0

print(1 or 0)   # 1
print(0 or -1)  # -1
print(-1 or 1)  # -1

a = 1
b = 0
c = 3
# 2 진법으로 계산, 비트연산
print(a|c) # 001 | 011 => 011 => 3 
print(b|c) # 000 | 011 => 011 => 3
print(a&b) # 001&000 => 000 => 0
print(a&c) # 001&011 => 001 => 1
print(c&a) # 011&001 => 001 => 1

