import sys
sys.stdin = open("input_simple.txt","r")


pws = ["3211","2221","2122","1411","1132","1231","1114","1312","1213","3112"]
# 2진수 암호해제 함수
def password(item):
    lst = "0" + item + "0"

    pw_data = []
    pw_data.append(0)
    cnt = 0
    for i in range(len(lst)):
        if len(pw_data) == 1 and lst[i] == "0" and cnt == 0:
            continue
        if len(pw_data) == 1 and lst[i] == "1":
            cnt += 1
            continue
        prev = lst[i-1]
        now = lst[i]
        if prev != now :
            pw_data.append(cnt)
            cnt = 1
            continue
        else:
            cnt += 1
    # print(pw_data)
    pw_data[0]  = 7-pw_data[1] - pw_data[2]- pw_data[3]
    result = []
    for d in range(8):
        ix = tuple(pw_data[4*d:4*d+4])
        if ix in pws:
            result.append(pws.index(ix))
        else:
            return 0
    Sum = 0
    for i in range(8):
        if i%2 ==0:
            Sum += 3*result[i]
        else :Sum += result[i]
    if Sum % 10 != 0:
        return 0
    return sum(result)

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]
    data_set = []
    prev= ''
    for i in range(n):
        # 우선 주변 0 strip
        arr_i = arr[i].strip("0")
        # arr_i가 공백이 아닌경우에만
        if arr_i:
            final = password(arr_i)
            break
    print(f"#{tc} {final}")

