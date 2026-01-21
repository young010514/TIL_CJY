arr_a = [2,1,2,4,5]
arr_b = [[2,5,3],[4,5,7],[8,7,2]]
num = int(input())
result = 0
for x in arr_a :
    if x == num : result += 1
for inner in arr_b :
    for x in inner:
        if x == num : result += 1
print(result)