# 변수 선언
a = 1   # 정수값 1
b = "1" # 문자 1 (문자가 여러개 = 문장, 문자열)
c = True    # True False (Boolean Type)
print(a)
# print(a + b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

a, b, c = 1, 2, 3
print(a, b, c)

a = b = 6 
print(a, b)

integer = 3
print(type(integer))  # <class 'int'>

string = '문자열'
print(type(string))  # <class 'str'>

boolean = True
print(type(boolean))  # <class 'bool'>

# type 변환 (형변환)
string_num = '3'
# print(string_num + 5)  # TypeError: can only concatenate str (not "int") to str

print(int(string_num) + 5) 

# 문자열 출력
name = '최민호' # 문자열
age = 42 # 정수값

# 도전!
# 제 이름은 최민호 이고 42살 입니다.

# % string      # 참고
print("제 이름은 %s 이고 %d살 입니다" % (name, age))

# str.format    # 참고
print("제 이름은 {0} 이고 {1}살 입니다".format(name, age))

# f-string      # 필수
print(f'제 이름은 {name} 이고 {age}살 입니다.')



# ===========================================
# 리스트
mylist = ['java', 'Django', 'c++,' 'HTML', 'Python']
print(mylist[1])

# 리스트의 길이(원소의 개수)
print(len(mylist))

# 인덱싱
print(mylist[1:4])

# 연습문제 
# 주말동안 맛있게 먹은 음식 이름으로 채워진 리스트 선언해주세요.

foodlist= ['밥','반찬' ,'국','고기','야채']
# 첫번째 값 출력

print(foodlist[0])

# 두번째 값을 초밥으로 바꾸기
foodlist[1]='초밥'
print(foodlist)


# ======================================================================
# 딕셔너리
dic = {'이름':'최민호', '나이':42, '성별':'남'}
print(dic['성별'])
# 딕셔너리는 key로 접근해서 value를 출력하는 것이 기본 형태

# 딕셔너리 value변경
dic['이름']='홍길동'
print(dic)
print(dic['이름'])

# 문제
phone_number={
    '최':'010',
    '민':'9353',
    '호':'6698',
    'studyterm':{'stcamp':'3days',
             'python':'2weeks',
             'algorithm':'6weeks'},
    111:'굳굳'}


# 2-1. python 공부 기간을 출력해 보세요 (2weeks)
print(phone_number['studyterm']['python'])

movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}

# 1. 영화의 제목을 출력하시오.
print(movie['movieInfo']['movieNm'])

# 2. 다음 movie의 감독의 영어 이름을 출력하시오.
print(movie['movieInfo']['directors'][0]['peopleNmEn'])


# 3. 다음 movie의 배우의 인원을 출력하시오.
print(len(movie['movieInfo']['actors']))
