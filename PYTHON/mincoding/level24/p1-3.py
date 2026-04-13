n = int(input())
arr= [input() for _ in range(n)]
lst = []
def abc(level, data):
    if level == 4:
        if sorted(data) not in lst : lst.append(sorted(data))
        return
    for i in range(n):
        if arr[i] not in data :
            data.append(arr[i])
            abc(level + 1, data)
            data.pop()
abc(0,[])
cnt =0
for lst1 in lst:
    st1 = list("CHRISTMAS")
    lst = []
    for i in lst1:
         lst += list(i)
    if sorted(st1) == sorted(lst): cnt +=1
print(cnt)