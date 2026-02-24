# 함수를 정의한 다음에 호출한다

def kfc():
    abc()
    print("#")
def abc():
    print('ㄱㄱ')

kfc()  # 정상 호출  
print("@@")
# 출력 순서

# ㄱㄱ
# #
# @@

# ====================================

# 1. 함수가 정의된 다음에 호출을 한다
# 2. 함수가 끝나고 난 후에는 --> 해당 ㅎ마수를 호출한 곳으로 돌아간다

def getsum(a, b):  # a , b == parameter 매개변수
    return a + b
def getsum(a, b):  # a , b == parameter 매개변수
    return  # 함수 종료를 의미
    print("##") # 이후의 코드는 함수를 호출해도 실행되지 않음


ret = getsum(3,7) # 3, 7 arguments 인자값

print(ret)


# =======================================
def getsum(x, y, k =8) : # k는 default parameter로 정의할때 다른 변수들의 뒤에 위치하도록 해야함
    return x+y+k
result = getsum(76,4)
print(result)

# ======================================
# packing
# 값 여러개를 하나의 변수 안에 넣어주는 것

num = [1, 2, 3, 4, 5]
num2 = (1, 2, 3, 4, 5)


# unpacking
# 남는 값을 풀기
# *를 이용해 풀어낼수도 있음

a, b, c, d, e = num
a, b, c, d, e = num2
a, b, *c = num  # a = 1, b = 2, c = [3,4,5]
print(a, b, c)
a, b, *c = num2  # a = 1, b = 2, c = [3,4,5]
                            #  ** 튜플이었지만 리스트로 자동 형변환 되어서 출력
print(a, b, c)

a, *b, c = num  # a = 1, b = [2,3,4], c = 5
print(a, b, c)


def getsum(*a):
    print(type(a))  # tuple     # list로 형변환? 안되고 tuple
    return a[0] + a[1] + a[2]

ret = getsum(1,2,3)

print(ret) # 6


# 키워드 가변인자

def print_info(**test):
    print(test)

print_info(kevin=1, bob=2, kate = 3)


# 함수에서 사용하는 변수 - 지역변수, 전역변수(global 변수)
aa, bb= 7,6
def abc():
    global aa,bb
    print(aa, bb) # 7, 6 
    aa, bb =3,5
    print(aa,bb) # 3, 5
abc()
print(aa,bb) # 3, 5
print("*"*50)

# 예시

# 글로벌 변수(전역변수)의 값을 다른 함수에서 바꿀 시에는 반드시 global을 명시해야함

def kfc():
    print(aa, bb, '****')
    # aa += 1  # global을 명시하지 않은 상태에서 값을 변경하려는 시도 
            #  즉,메모리 값을 변경하려는 시도를 진행하는 순간부터 error 발생
            # 근데 왜 이건 위의 print도 안되는건지 모르겠음
    # bb +=1 
    print(aa, bb)
    
def test():
    global aa, bb
    aa= 3
    bb =5
    print(aa, bb)

test()
kfc()

# 내장함수
# map

num = ['1','2','3']
lst1 = []
for i in num :
    lst1.append(int(i))

print(lst1)
print("++++++"*10)
# 위와 동일한 방법
# map 문법 : map(적용시킬 함수, 적용이 될 객체(순회가능한))
lst_map = map(int, num)
print(lst_map)   # map이라는 객체를 return

# a = input()   # 하나의 문자열 입력받기
# b = input().split()  
# b = list(input().split())  
# print(b, type(b))


# zip 내장함수
# 각각의 원소를 잘라서 튜플로 저장하는 함수
a = '12345'
b = 'qwert'
c = 'asdfg'
ret = zip(a,b)
print(ret)          # <zip object at 0x00000261ECA844C0>
print(list(ret))    # [('1', 'q'), ('2', 'w'), ('3', 'e'), ('4', 'r'), ('5', 't')]

for i in zip(a,b,c):    # 리스트로 출력
    print(list(i))

for x,y,z in zip(a,b,c):  # 값만 출력
    print(x,y,z)


# filter (적용시킬함수, 적용할 곳)
# 참인 값만 반환해주는 함수다

num = list(range(1, 8)) # [1,2,3,4,5,6,7]

def get_even(value):
    return True if value %2 ==0 else False

ret = filter(get_even, num)
print(list(ret))


# lambda 함수 (익명함수)


# 방법1
ret = (lambda a, b: a + b)(3,5)
print(ret)
# 방법2
ret = (lambda a,b : a+b)
print(ret(3,5))

# 예시
# 두 리스트의 값을 세로로 더했을 때 함을 각각 출력하기
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
print(list(map(lambda a,b : a+b, lst1, lst2)))
# ver1
lst3 = [0]*5
for i in range(5):
    lst3[i] = lst1[i]+ lst2[i]
print(*lst3)

# ver2
ret = (lambda x,y :x + y)
lst3 = map(ret, lst1,lst2)
print(*lst3)
# ver2를 한줄로
lst3=map(lambda x,y:x+y, lst1, lst2)

# ======================================
# 재귀함수(recursion)
# 함수가 자기 자신을 호출하는 함수

print("**********재귀함수**********************")
def abc(level):
    if level == 11:
        return
    print(level, end=' ')   
    abc(level+1)
    print(level, end=' ')   
abc(0)
# 0 1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1 0



# 예시
# n 개의 주사위 던져서 나오는 모든 경우 출력

n = int(input())
path = [0]*n

def abc(level):
    if level == n :
        print(*path)
        return
    for i in range(1,7):
        path[level]=i
        abc(level+1)
        path[level]=0
abc(0)