# def abc(level):
#     if level == 3:
#         return
#     print(level,end=' ')
#     abc(level+1)
#     print(level, end=' ')
# abc(0)


# 1 2 3 4 5 4 3 2 1
def abc(level):
    print(level, end=' ')
    if level == 5:
        return
    abc(level+1)
    print(level, end=' ')

abc(1)

print("\n***********")

# level=3일때
# 0 1 2 3

def abc(level):
    print(level,end=' ')
    if level == 3 :return
    abc(level+1)
abc(0)


print("\n***********")

# level=3일때
# 0 1 2
def abc(level):
    if level==3 :return
    print(level,end=' ')
    abc(level+1)
abc(0)


print("\n***********")

# level=3일때
# 2 1 0
def abc(level):
    if level==3 :return
    abc(level+1)
    print(level,end=' ')
abc(0)




print("\n***********")

# level=3일때
# 0 1 2 3 2 1 0
def abc(level):
    print(level,end=' ')
    if level==3 :return
    abc(level+1)
    print(level,end=' ')

abc(0)


print("\n***********")

# level=3일때
# 0 1 2 2 1 0
def abc(level):
    if level==3 :return
    print(level,end=' ')
    abc(level+1)
    print(level,end=' ')

abc(0)


print("\n***********")

# 1차원 리스트에 정수 입력
# 예 > arr = [12, 65, 34, 23, 34]
arr = [12, 65, 34, 23, 34]
# arr = list(map(int,input().split()))
def abc(idx):
    print(arr[idx],end=' ')
    if idx == len(arr)-1:
        return
    abc(idx +1)
    print(arr[idx], end=' ')
abc(0)


# ======================================
print("\n***********")

def abc(level):
    if level ==2:
        return
    # abc(level +1 )
    # abc(level +1 )
    for i in range(2):
        abc(level +1)

abc(0)
