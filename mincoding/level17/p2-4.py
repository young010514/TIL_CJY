arr = [list('GKT'),list('PAC')]

a,b = input().split()
result = 0
for inner in arr:
    if a in inner: result += 1   
    elif b in inner: result += 1   
if result == 2:
    print("대발견")
elif result == 1:
    print("중발견")
else:
    print("미발견")