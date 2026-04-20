arr = [list('A79TKQ'), list('MINCOD')]

a, b= input().split()

result = ['없음','없음']
for inner in arr:
    if a in inner:
        result[0] = '존재'
    if b in inner :
        result[1] = '존재'

print(f'{a} : {result[0]}')
print(f'{b} : {result[1]}')