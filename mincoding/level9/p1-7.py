data = []
for i in range(6):
    a, b = map(int, input().split())
    data.append([a, b])
change_num = 0
for x in data:
    if x[0] < x[1] :
        x[0], x[1] = x[1], x[0]
        change_num +=1
for p in data :
    print(p[0], p[1])
print(f'{change_num}명')
