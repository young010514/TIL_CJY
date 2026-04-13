arr =['A',"B",'C','D']
result = []

def abc(level, st1):
    if level == 3:
        result.append(st1)
        # print(st1)
        return
    for i in range(4):
        abc(level+1, st1 + arr[i])
        # st1 -= arr[i]

abc(0,'')
i = input().strip()
print(f"{result.index(i) +1}번째")