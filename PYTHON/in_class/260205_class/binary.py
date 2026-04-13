# n = int(input())
# arr = list(map(int,input().split()))
# target=  int(input())
#
# def binary_search(st,ed,target):
#     while 1:
#         mid = (st+ed) // 2
#         if target == arr[mid]:
#             return 1
#
#         # startpoint나 endpoint 옮기기
#         elif arr[mid] > target: ed= mid-1
#         elif arr[mid] < target: st = mid + 1
#
#
#         if st > ed : return 0 # 못찾으면 0 리턴
#
#
#
# arr.sort()
# ans = binary_search(0,n-1,target) # start, end, target
# if ans :
#     print("find")
# else:print("cannot")

# parametric search


# def binary_search(st,ed,battery):
#     while 1:
#         if st > ed:
#             return ed + 1
#
#         mid = (st+ed) // 2
#
#         if battery[mid] == "#":
#             st = mid+1
#         elif battery[mid] == "_":
#             ed = mid -1

def parametric_search(st,ed):
    Max = -1
    while 1 :
        mid = (st+ed) // 2
        if battery[mid] == "_": ed = mid -1
        elif battery[mid] == "#" :
            st = mid +1
            Max = mid
        if st > ed :
            return Max + 1



battery = "######____" # 60%
print(f"{parametric_search(0,len(battery)-1) * 10 }%")

battery = "__________" # 0%
print(f"{parametric_search(0,len(battery)-1) * 10 }%")

battery = "##########" # 100%
print(f"{parametric_search(0,len(battery)-1) * 10 }%")


# 워드작업 중 정전으로 인하여 컴퓨터가 강제로 종료가 되었습니다.
# 다시 전기가 들어어 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을때 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그래밍을 완성해 주세요.
# 시간복잡도 (On^2)보다 빨라야 합니다.

# 6*10 size 리스트 (배열)

curser=[
    '##########',
    '##########',
    '###_______',
    '__________',
    '__________',
    '__________']
def parametric_search(st,ed):
    # 가로부터 찾기
    while 1:
        mid = (st + ed) // 2
        if curser[mid][-1] == "#":
            st = mid +1
        elif curser[mid][-1] == "_":
            ed = mid -1
        if st > ed :
            x = ed+1
            break


    st, ed = 0,len(curser[0])-1
    while 1:
        mid = (st + ed) // 2
        if curser[x][mid] == "#":
            st = mid +1
        elif curser[x][mid] == "_":
            ed = mid -1
        if st > ed :
            y = ed +1
            break

    return x,y
x,y = parametric_search(0,len(curser)-1)
print(f"{x * 10 + y}%")
