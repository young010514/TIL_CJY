st = 'ATKPTCABC'
a,b= input().split()
id1 = st.index(a)
id2 = st[::-1].index(b)
result = len(st) - id1 - id2 - 1
print(result)