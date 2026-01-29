arr = [3,7,4,9]
inp = list(map(int,input().split()))
def isSame(arr1, arr2):
    result = 'pass'
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            result = "fail"
            break
    print(result)
isSame(arr, inp)