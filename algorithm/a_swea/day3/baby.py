import sys
sys.stdin = open("input_baby.txt","r")

def check(arr):
    checkarr = [0]*10               # 현재 있는 숫자들 카운트할 배열
    for i in range(len(arr)):
        checkarr[arr[i]] += 1
    if 3 in checkarr : return 1     # 동일한 숫자 3
    for i in range(8):
        chk = 1                     # 연속된 숫자가 있는지 확인
        for d in range(3):
            if checkarr[i+d] == 0 :
                chk = 0             # 0이 있다면 chk =0으로 변경하고 다음 거 확인
                break
        if chk == 1 : return 1      # 3번 연속된 숫자가 있으므로 return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    result = 0
    for i in range(6):
        lst1 = arr[0:2*i+2:2]   # 플레이어 1
        lst2 = arr[1:2*i+3:2]   # 플레이어 2
        if check(lst1) == 1:
            result = 1
            break
        elif check(lst2) == 1:
            result = 2
            break
    print(f"#{tc} {result}")
