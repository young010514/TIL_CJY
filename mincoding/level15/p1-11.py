arr = [
    input(),
    input(),
    input(),
    input(),
]
result =[0,0]
for i in arr:
    if 'A' in i: result[0] = 1
    if 'B' in i : result[1] = 1
if sum(result) == 2:
    print("대발견")
elif sum(result) == 1:
    print("중발견")
else:print("미발견")