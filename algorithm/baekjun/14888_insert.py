n = int(input())
nums = list(map(int,input().split()))
lst = list(map(int,input().split()))    #   + - * /
datas = []

def dfs(level, arr):
    if level == n-1 :
        datas.append(arr)
        return
    for i in range(4):
        if lst[i] == 0 :continue
        lst[i] -= 1
        dfs(level+1, arr+[i])
        lst[i] +=1
dfs(0,[])
result = []
def main(data):
    global result
    nums1 =nums[::-1]
    idx = 0
    while len(nums1) > 1:
        temp1 = nums1.pop()
        temp2 = nums1.pop()
        plus = data[idx]
        if plus == 0:
            rst = temp1 + temp2
        elif plus == 1:
            rst = temp1 - temp2
        elif plus == 2:
            rst = temp1 * temp2
        else:
            if temp1 > 0 : rst = temp1 // temp2
            else: rst = -1*(-temp1 // temp2)
        nums1.append(rst)

        idx += 1
    result.append(nums1[0])

for data in datas :
    main(data)
result.sort()
print(result[-1])
print(result[0])


