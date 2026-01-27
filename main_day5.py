# set (중복을 허용하지 않는 데이터들의 묶음)
s = {1,2,3,4,5}

# 값 추가
s.add(6) # 값 한개 추가
print(s) 
s.update([11,22,13,14,15]) # 값 여러개 추가
print(s)

# 값 삭제
s.remove(11) # remove 사용시 없는 값 제거하면, key error 난다
s.discard(221) # discard 사용시 없는 값 제거해도 에러안남
print(s)
s.clear()  # 값 모두 비우고 빈 set만들기


# =====================================

# 집합
s1 = {1,2,3,4}
s2 = {2,4,6,8}

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 부분집합
# s1의 항목이 모두 s2 에 들어가 있으면 True 반환
print(s1 <= s2)
print(s1.issubset(s2))

# ==================================
# 딕셔너리 값 추가하기
# 방법1 

# [연습문제]
st={'kevin':1,'john':2,'bob':[3,4,5]}

ls_key=['asdf','zcv','qwe']
ls_value=[1,2,3]

# ls_key 리스트의 원소를 key로 그리고 ls_value의 원소로 값으로 하는 딕셔너리를
# st 딕셔너리에 추가하기
for k,v in zip(ls_key, ls_value):
    st[k] = v
print(st)

# 출력결과: {'kevin': 1, 'john': 2, 'bob': [3, 4, 5], 'asdf': 1, 'zcv': 2, 'qwe': 3}
# 방법1
for i in range(3):
    st[ls_key[i]] = ls_value[i]

# 방법2 update
for i in range(3):
    st.update({ls_key[i] : ls_value[i]})

# 방법3 zip
temp = dict(zip(ls_key, ls_value))
print(st.update(temp))

# 방법 1,2,3번의 공통점 !! 없는 key라면 새로운 value 추가
#                       있는 값이라면 업데이트 됨


# 원본 데이터를 보호하려면? ? ==> setdefault()
# 없는 키라면, 새로운 value 추가하고 있는 key라면 업데이트 안되고 원본 데이터를 보존한다
for i in range(3):
    st.setdefault(ls_key[i], ls_value[i])
print(st)
st.setdefault('amy', 'korea')  # {'kevin': 1, 'john': 2, 'bob': [3, 4, 5], 'asdf': 1, 'zcv': 2, 'qwe': 3, 'amy': 'korea'}
print(st)
st.setdefault('kevin', 'aaaaa')  # {'kevin': 1, 'john': 2, 'bob': [3, 4, 5], 'asdf': 1, 'zcv': 2, 'qwe': 3, 'amy': 'korea'}
                                # 원본값 보존됨
print(st)


# 값 삭제

# del
st={'kevin':1,'john':2,'bob':[3,4,5]}
# del st['kevin']  # 없는 key 삭제하려면 error
print(st)

# pop 이용 반환값 있음
st.pop('kevin')
print(st)

# KeyError 내기 싫을때도 pop 사용가능
st.pop("kein", '없음')   # key가 없을경우 default 값을 세팅 해둬야 함
print(st)



# dict 기본 메소드

st={'kevin':1,'john':2,'bob':[3,4,5]}

# key만 가지고 리스트 만들기
lst = st.keys()
print(list(lst))

lst = st.values()
print(list(lst))

lst = st.items()
print(list(lst))


# dictionary 왜쓰냐? 다른 언어에는 이런거 없던데 왜 파이썬에만 있나?

# 다른 언어에서는 해시라는 자료 구조를 제공하는 함수를 직접 불러다 쓰거나
#   C언어의 경우 해시를 직접 구현해서 사용함

# 자료구조 - 데이터를 어떻게 저장하고 관리할 것인가? 를 다루는 분야

# direct address table(자료구조)
# 저장된 값을 다른 배열의 인덱스로 활용하는 자료 구조

# arr 배열에 10개의 숫자를 입력 ( 1~9 사이의 정수 값 입력받는다고 가정 )
arr = [1,5,3,4,8,5,7,3,1,9]
# arr 배열에 입력된 값 중 각각의 정수가 몇 개씩 입력되었는지? 출력하기
for i in range(10):
    cnt = 0
    for num in arr :
        if i == num:
            cnt += 1
    print(f'{i}의 개수는 {cnt}개')


# 배열 안에 bucket이라는 배열의 인덱스로 활용해서
# 빠른 속도 냄


# open address 방식
arr = ['apple','banana','dragonfruits','apple','avocado','carrot']
bucket = [0]*10

def hash(key):
    return ord(key[0]) % 3


for k in arr :
    hashcode = hash(k)

    while bucket[hashcode] !=0 :
        hashcode = (hashcode + 1) % 10
    bucket[hashcode] = k
print(bucket)
