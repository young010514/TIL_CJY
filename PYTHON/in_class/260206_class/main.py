arr = [3,4,5,1,6,9]

# Sum 매개변수를 사용해서 누적 합 출력하기
# 3 7 12 13 14 28
def abc(x, idx):
    if idx == len(arr):
        return
    x += arr[idx]
    print(x, end= ' ')
    abc(x, idx+1)
abc(0,0)

print("\n*****************")

def abc(level,Sum):
    print(Sum, end=' ')
    if level == 5:
        return
    abc(level + 1, Sum + arr[level + 1])
abc(0, arr[0])


print("\n*****************")
# Sum을 전역변수로 놓고 누적 합 출력
Sum =0
def abc(idx):
    if idx == len(arr):
        return
    global Sum
    Sum += arr[idx]
    abc(idx +1)
abc(0)
print(Sum)


print("\n*****************")

# Sum이라는 전역 변수를 이용해서 누적 합 출력하기

Sum =0
def abc(idx):
    if idx == len(arr):
        return
    global Sum
    Sum += arr[idx]
    data = Sum
    abc(idx +1)
    print(data, end=' ')
abc(0)

# 강사님코드
print("\n*****************")
arr = [3, 4, 5, 1, 6, 9]
Sum = arr[0]


def abc(level):
    global Sum

    if level == 5:
        print(Sum,end=' ')
        return
    Sum += arr[level + 1]
    abc(level + 1)
    Sum -= arr[level +1]
    print(Sum, end=' ')
abc(0)

print("\n*****************")
# Sum이라는 매개 변수(지역변수)를 이용해서 누적 합 출력하기
arr=[3,4,5,1,6,9]

def abc(level,Sum):


    if level==5:
        print(Sum, end=' ')
        return

    abc(level+1,Sum+arr[level+1])
    print(Sum, end=' ')

abc(0,arr[0])


print("\n*****************")
print("\n*****************")

# 3개의 카드 묶음이 있는데, 각 묶음에서 카드 1장씩 뽑았을 때 나올 수 있는 합을 모두 출력하기

# branch = 4, level = 3에서 리턴

arr= [3,7,1,2]

def abc(level, Sum):
    if level ==3:
        print(Sum, end=' ')
        return
    for i in range(4):
        abc(level+1, Sum + arr[i])


abc(0,0) # level, Sum



print("\n*****************")

# 3개의 카드 묶음이 있는데, 각 묶음에서 카드 1장씩 뽑았을 때 나올 수 있는 합을 모두 출력하기

# branch = 4, level = 3에서 리턴

arr= [3,7,1,2]
Sum = 0
def abc(level):
    global  Sum
    if level ==3:
        print(Sum, end=' ')

        return
    for i in range(4):
        Sum += arr[i]
        abc(level+1)
        Sum -= arr[i] # 출력할때 마지막에 더한 값은 빼고 다시 + 가 되기 위해

abc(0) # level


print("\n*****************")

# 3개의 카드 묶음이 있는데, 각 묶음에서 카드 1장씩 뽑았을 때 나올 수 있는 합을 모두 출력하기

# branch = 4, level = 3에서 리턴

arr= [3,7,1,2]
Sum = 0
def abc(level):
    global  Sum
    if level ==3:
        print(Sum, end=' ')

        return
    for i in range(4):
        Sum += arr[i]
        abc(level+1)
        Sum -= arr[i] # 출력할때 마지막에 더한 값은 빼고 다시 + 가 되기 위해

abc(0) # level
print("\n#######################")

# 그리디 알고리즘 대신 재귀함수를 이용해 동적 알고리즘 사용해보기
# 210원을 110, 70,10원짜리로 거슬러 주되, 가장 작은 동전의 갯수를 넣기
n = 210
coin = [110,70,10]
Min_level =100
def abc(level, Changes):
    global  Min_level
    if level > 100:
        return

    if Changes < 0: # 백트레킹
        return

    if level > Min_level : # 백트레킹
        return

    # 최소레벨을 갱신
    if Changes == 0 :
        Min_level = level if level < Min_level else Min_level
        return

    for i in range(3):
        abc(level + 1, Changes - coin[i])

abc(0,n)
print(Min_level)



