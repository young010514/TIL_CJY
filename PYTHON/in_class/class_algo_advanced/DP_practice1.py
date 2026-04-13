arr =[0,7,-3,-5,-4,-2,6,5,-9,-1,0]

result = [0]*len(arr)
def dp():
    global result
    for i in range(1,11):
        data = result[i-1]
        if i-2 >= 0 :
            data = result[i-2] if data < result[i - 2] else data
        if i% 2 == 0 :
            data = result[i//2] if data < result[i // 2] else data
        result[i] = data + arr[i]

dp()
print(result)
