import sys
sys.stdin = open("input_scan.txt","r")


# 16진법에서 2진법으로
def to_binary(s):
    num_16 = "0123456789ABCDEF"
    result = []
    for i in s:
        num = num_16.index(i)
        st = ''
        while num:
            st = str(num % 2) + st
            num //=2
        result.append(st.zfill(4))
    return ''.join(result).strip("0")
pws = ["211","221","122","411","132","231","114","312","213","112"]

# 2진수 암호해제 함수
def password(item):
    lst = item + "0"
    pw_data = [0]
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
    last_sum= 0
    for i in range(4):
        last_sum += pw_data[-i-1]
    pw_data[0] = last_sum - pw_data[1] - pw_data[2]- pw_data[3]

    return pw_data

def find_pw(lst):
    sum_4 = 0
    Sum = 0
    result = 0
    for i in range(4):
        sum_4 += lst[-i-1]
    if sum_4 % 7 !=0 : return 0

    if sum_4 != 7 :
        divide = sum_4 // 7
        for i in range(32):
            if lst[i] % divide != 0 : return 0
            lst[i] = lst[i] // divide
    for i in range(8):
        item = ''.join(list(map(str, lst[4*i+1:4*i+4])))
        if item not in pws: return 0
        rst = pws.index(item)
        result += rst
        if i % 2 ==0 : Sum += 3* rst
        else:Sum += rst
    if Sum % 10 != 0: return 0
    return result


# 문자열 길이에 신경쓰지 말고 뒤에서부터 ?
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]
    data_set = []
    final = 0
    prev= ''
    for i in range(n):
        # 우선 주변 0 strip
        arr_i = arr[i].strip("0")
        # arr_i가 공백이 아닌경우에만
        if arr_i:
            # 한줄에 여러 암호코드가 있을 수 있음 이때 임의로 00000으로 split 해봄
            s_strip = arr[i].strip("0").split("00000")
            for item in s_strip:
                # 00000으로 split 하면서 주변 0들이 제거되지 않았을 수 있으므로 strip("0")
                item_strip = item.strip("0")
                # strip 결과가 공백이 아니고, 준비된 data_set에 저장되지 않은 경우에만 append
                if item_strip and item_strip not in data_set :
                    data_set.append(item_strip)

    # 저장된 data_set 내의 암호코드로 계산하기
    find_lst = []
    for item in data_set:
        bin_item = to_binary(item)
        if bin_item not in find_lst:find_lst.append(bin_item)

    for i in find_lst:
        pw_data = password(i)
        final += find_pw(pw_data)
    print(f"#{tc} {final}")

