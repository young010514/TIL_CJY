arr = ["BBQWORLD",'KFCAPPLE','LOT']
s = input()
cnt =0
for i in arr:
    cnt += list(i).count(s)

print(cnt)