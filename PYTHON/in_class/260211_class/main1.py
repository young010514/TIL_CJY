# 두 라인에서 숫자 1개씩 번갈아 가며 선택할때
# 라인1에서 1개 라인2에서 1개... 번갈아 가며 뽑습니다.
# (각 라인의 숫자는 1번씩만 사용하며 숫자를 뽑습니다.)
# 첫 번째 숫자 선택한 값에 *1 을하고
# 두번째 택한 값에 *2를 하고
# 세번째 택한 값에 *3.. 씩
# 모든 값에 1씩 증가되는 값으로 가중치를 곱한 후
# 모두 더했을떄 0에 가장 가까운 수를 구하고자 합니다.
# 이때 총 합이 몇이 될까요??
line1=[5,2,7,-5,-7,9]
line2=[4,-5,-7,9,-5,3]

used1 = [0] * 6
used2 = [0] * 6

Min = 8e8
def dfs(level,Sum):
    global Min
    if level > 12:
        if abs(Sum) < abs(Min) :
            Min = Sum
        return


    if level % 2==0:
        for i in range(6):
            if used2[i] == 0:
                used2[i] = 1
                dfs(level +1, Sum + line2[i] * level)
                used2[i] = 0
    else:
        for i in range(6):
            if used1[i] == 0:
                used1[i] = 1
                dfs(level +1, Sum + line1[i] * level)
                # 원상복구!
                used1[i] = 0


dfs(1,0)
print(Min)
