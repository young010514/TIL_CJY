arr =[]
for i in range(3):
    arr.append(input())
result =0
for inner in arr:
    if "M" in inner:
        result = 1
if result :print("M이 존재합니다")
else:print("M이 존재하지 않습니다")