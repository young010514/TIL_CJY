arr = input().split()
index_result = []
cnt = 0
for index, x in enumerate(arr):
    if x == "A" :
        cnt += 1 
        index_result.append(index)
print(f"문자A는 {cnt}개발견")
[print(f"{x}번") for x in index_result]