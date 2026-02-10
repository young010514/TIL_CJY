arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0],
]
n = int(input())
used =[0]*len(arr)

def abc(visited):
    will_visit = []
    if not visited : return
    for idx in visited :
        if sum(arr[idx]) == 0 :
            continue
        for i in range(6):
            if arr[idx][i] == 1 and used[i] ==0:
                used[i] = 1
                will_visit.append(i)
    for i in will_visit:
        print(i)
    will_visit.sort()
    abc(will_visit)
print(n)
used[n] = 1
abc([n])
