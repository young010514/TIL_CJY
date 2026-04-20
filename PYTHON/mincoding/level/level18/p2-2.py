arr = list(map(int,input().split()))
if len(arr) != len(set(arr)):
    print("도플갱어 발견")
else:print('미발견')