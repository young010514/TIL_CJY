ty = int(input())
n = int(input())
lst = list(map(int,input().split()))
if ty == 1:
    result = [0] * 10
    for i in lst:
        result[i] +=1
    for i in range(1,10):
        print(f"{i}:{result[i]}개")
if ty == 2:
    if len(lst) == len(set(lst)) : print("중복없음")
    else:print("중복발견")