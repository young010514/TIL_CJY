lst = [3,4,1,1,2,6,8,7,8,9,10]
start = int(input())
def getSum(arr, i):
    result = 0
    for i in arr[i:i+5]:
        result += i
    return result
print(getSum(lst,start))