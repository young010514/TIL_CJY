a =list(input())
di = {}
m = 0
result = ''
for idx,i in enumerate(a):
    if m < a.count(i) :
        m = a.count(i) 
        result = i
print(result)