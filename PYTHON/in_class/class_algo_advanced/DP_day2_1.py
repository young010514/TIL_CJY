def lcs(s1,s2):
    len1,len2 = len(s1),len(s2)
    arr = [[0] * (len2+1) for _ in range(len1+1)]

    Max = 0
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s1[i-1] == s2 [j-1]:
                arr[i][j] = arr[i-1][j-1] +1
                Max = max(Max, arr[i][j])
            else: arr[i][j] = 0
    return Max
s1 = "BABJYP"
s2 = "ABCBJY"
print(lcs(s1,s2))

def lcs2(s1,s2):
    len1, len2 = len(s1),len(s2)
    arr= [[0] * (len2+1) for _ in range(len1+1)]
    for i in range(1,len1+1):
        for j in range(1,len2 + 1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1] +1
            else :
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    return arr[len1][len2]
s1 = 'BABJYP'
s2 = "ABCBJY"
print(lcs2(s1,s2))

n = int(input())
arr = list(map(int,input().split()))

result = [1] * n
for y in range(n):
    code = arr[y]
    for i in range(y):
        val = arr[i]
        if code > val:
            result[y] = max(result[i] + 1 , result[y])
print(max(result))

