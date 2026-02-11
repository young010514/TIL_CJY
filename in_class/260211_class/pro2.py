# a 50
# b 40
# c 99
# d 5
# e 25
# f 6
# g 37

# 서바이벌 선수와 전투력이 있을때
# a~f를 두 팀으로 만들어서 서바이벌 게임을 하고자 한다.
# 두 팀의 전투력 차이가 가장 적게하여 두 팀을 구성한다고 했을때
# 두 팀의 최소 전투력 차이는 몇이 되는가?
# 모든 선수는 서바이벌에 참가하며 1인팀도 가능합니다.

# name = list("abcdefg")
# power = [50,40,99,5,25,6,37]
# power_sum = sum(power)
# used = [0]*7
# Min = 21e5
#
# def dfs(level,prev, Sum):
#     global Min
#     if level == 6:
#         if abs(power_sum -2* Sum) < Min :
#             # print(Min)
#             Min = abs(power_sum - 2*Sum)
#         return
#     for i in range(prev,7):
#         dfs(level +1 ,i,Sum+power[i])
# used[0] = 1
# dfs(0,1,power[0])
# print(Min)


# 강사님 풀이
name = list("abcdefg")
power = [50,40,99,5,25,6,37]

Min = 21e8
total = sum(power)

def dfs(start,level,Sum):
    global Min, power
    against = 0
    against = total - Sum   # 상대편 전투력 확인 후

    gap = abs(Sum - against)    # 차이 확인
    Min = min(Min, gap) # 차이의 최소값 갱신

    if level == 6:
        return
    for i in range(start, 7):
        dfs(i+1, level+1, Sum + power[i])
dfs(0,0,0) # start, level, Sum
print(Min) # 2

