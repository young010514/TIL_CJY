a,b = input(),input()
cnt = abs(len(a) - len(b))
for i in range(min(len(a), len(b))):
    if a[i]!= b[i] :
        cnt +=1
print(cnt)
