import math
n = int(input())
m = int(input())
result = 1
prev = 1
def cnt(st,ed):  # st 부터 ed 까지 (ex. 1,3 => (1,2,3))
    data = [0] * (ed-st)
    rst = 1


    return rst

for i in range(m):
    num = int(input())
    if num-prev <= 1:
        prev=num+1
        continue

    result *= cnt(prev,num-1)
    prev=num+1
if n - prev >1 :
    result *= cnt(prev,n)

print(result)