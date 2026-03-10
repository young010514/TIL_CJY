s,t = map(int,input().split())
a,b= map(int,input().split())
m,n= map(int,input().split())
mlst = list(map(int,input().split()))
nlst = list(map(int,input().split()))
x,y = 0,0
for i in range(m):
    data = mlst[i] + a
    if s <= data <= t : x +=1
for i in range(n):
    data = nlst[i] + b
    if s <= data <= t : y +=1
print(x)
print(y)