import sys
sys.stdin = open("input_scan.txt","r")

hex_to_bin = {
    '0':'0000','1':'0001','2':'0010','3':'0011',
    '4':'0100','5':'0101','6':'0110','7':'0111',
    '8':'1000','9':'1001','A':'1010','B':'1011',
    'C':'1100','D':'1101','E':'1110','F':'1111'
}
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

    return pw_data

def find_pw(lst):
    sum_4 = 0
    Sum = 0
    result = 0
    for i in range(4):
        sum_4 += lst[-i-1]
    lst[0] = sum_4 - lst[1] - lst[2] - lst[3]
    # if sum_4 % 7 !=0 : return 0

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
    for i in range(n):
        # 우선 주변 0 strip
        arr_i = arr[i].strip("0")
        # arr_i가 공백이 아닌경우에만
        if arr_i:
            # 한줄에 여러 암호코드가 있을 수 있음 이때 임의로 00000으로 split 해봄
            s_strip = arr_i.split("00000")
            for item in s_strip:
                # 00000으로 split 하면서 주변 0들이 제거되지 않았을 수 있으므로 strip("0")
                item_strip = item.strip("0")
                # strip 결과가 공백이 아니고, 준비된 data_set에 저장되지 않은 경우에만 append
                if item_strip and item_strip not in data_set :
                    data_set.append(item_strip)

    # 저장된 data_set 내의 암호코드로 계산하기
    find_lst1 = []
    for item in data_set:
        bin_lst = []
        for i in item:
            bin_lst.append(hex_to_bin[i])
        bin_item = ''.join(bin_lst).strip("0")
        pw_data = password(bin_item)
        if pw_data not in find_lst1:
            if len(pw_data) == 32 : find_lst1.append(pw_data)
        if len(pw_data) == 64:
            pw_data[32] = 0
            if pw_data[:32] not in find_lst1 : find_lst1.append(pw_data[:32])
            if pw_data[32:] not in find_lst1 : find_lst1.append(pw_data[32:])
    for i in find_lst1:
        final += find_pw(i)

    print(f"#{tc} {final}")

