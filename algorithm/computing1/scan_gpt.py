import sys

sys.stdin = open("input_scan.txt", "r")


# 16진법에서 2진법으로
def to_binary(s):
    num_16 = "0123456789ABCDEF"
    result = []
    for i in s:
        num = num_16.index(i)
        st = ''
        while num:
            st = str(num % 2) + st
            num //= 2
        result.append(st.zfill(4))
    return ''.join(result).strip("0")


pws = ["211", "221", "122", "411", "132", "231", "114", "312", "213", "112"]


# 2진수 암호 해제 함수
def password(item):
    lst = item + "0"  # '0'으로 패딩
    pw_data = [0]
    cnt = 0
    for i in range(len(lst)):
        if len(pw_data) == 1 and lst[i] == "0" and cnt == 0:
            continue
        if len(pw_data) == 1 and lst[i] == "1":
            cnt += 1
            continue
        prev = lst[i - 1]
        now = lst[i]
        if prev != now:
            pw_data.append(cnt)
            cnt = 1
            continue
        else:
            cnt += 1

    last_sum = 0
    for i in range(4):
        last_sum += pw_data[-i - 1]
    pw_data[0] = last_sum - pw_data[1] - pw_data[2] - pw_data[3]

    return pw_data


def find_pw(lst):
    sum_4 = 0
    Sum = 0
    result = 0

    # 길이가 충분한지 확인하고 마지막 4개 값을 더하기
    if len(lst) < 4:
        return 0  # 길이가 부족하면 0을 반환

    for i in range(4):
        sum_4 += lst[-i - 1]

    if sum_4 % 7 != 0:
        return 0

    if sum_4 != 7:
        divide = sum_4 // 7
        for i in range(32):
            if lst[i] % divide != 0:
                return 0
            lst[i] = lst[i] // divide

    for i in range(8):
        if 4 * i + 4 <= len(lst):  # 인덱스 범위를 확인하여 슬라이싱을 진행
            item = ''.join(list(map(str, lst[4 * i + 1:4 * i + 4])))
            if item not in pws:
                return 0
            rst = pws.index(item)
            result += rst
            if i % 2 == 0:
                Sum += 3 * rst
            else:
                Sum += rst
        else:
            return 0  # 리스트 범위를 벗어나면 0을 반환

    if Sum % 10 != 0:
        return 0
    return result


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    data_set = []
    final = 0

    for i in range(n):
        arr_i = arr[i].strip("0")
        if arr_i:
            s_strip = arr[i].strip("0").split("00000")
            for item in s_strip:
                item_strip = item.strip("0")
                if item_strip and item_strip not in data_set:
                    data_set.append(item_strip)

    find_lst = []
    for item in data_set:
        bin_item = to_binary(item)
        if bin_item not in find_lst:
            find_lst.append(bin_item)

    for i in find_lst:
        pw_data = password(i)
        final += find_pw(pw_data)

    print(f"#{tc} {final}")