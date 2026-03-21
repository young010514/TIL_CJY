# 2,8,16진수로 바꿔보기
# 내장함수
a = 13
b = bin(a)
c = oct(a)
d = hex(a)
print(b,c,d)


# 2,8,16 진수를 10진수로 바꾸기
print(int(b,2))
print(int(c,8))
print(int(d,16))


# 2진수의 값을 16진수로 바꿔서 출력해보기
a='001111001010111010010011'

for i in range(0,len(a),4):
    r = a[i : i+4]  # 4개씩 자르기
    r2 = int(r,2)   # 10진수로 바꾸기
    r3 = hex(r2)    # 16진수로 바꾸기
    print(r3[2].upper(), end='')    # 앞에 진법 표기법 제거 후 알파벳은 대문자로 표기
print()

# for 문없이
a='001111001010111010010011'
bin1 = int(a,2)
print(hex(bin1)[2:].upper())


