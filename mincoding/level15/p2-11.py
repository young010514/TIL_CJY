arr = list("APPLET")
inp = input().split()
cnt =0
for i in inp:
    cnt += arr.count(i)
print(f"{cnt}개 맞추었습니다")