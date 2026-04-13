# 삽입 정렬
lst = [4,7,1,5,3]
result = []
for i in range(len(lst)):
    result.append(lst[i])
    for j in range(i,0,-1):
        if result[j - 1] > result[j]:
            result[j-1], result[j] = result[j], result[j-1]
        else:break
print(result)