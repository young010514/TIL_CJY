n = int(input())
y = n // 5
x = 0
while y >= 0:
    if (n-y * 5) % 3 == 0 :
        x = (n-y * 5)//3
        break
    y -= 1
if y <0 or x < 0 : print(-1)
else:print(x+y)