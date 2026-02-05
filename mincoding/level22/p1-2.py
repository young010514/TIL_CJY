arr = [input() for _ in range(3)]
cnt =0
for i in range(3):
    if arr[i].strip() == arr[(i+1) % 3].strip():
        cnt += 1

if cnt == 3: print("WOW")
elif cnt == 1:print("GOOD")
else:print("BAD")