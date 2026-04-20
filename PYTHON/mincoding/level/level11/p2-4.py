arr = [['a','b','a','c','z'],['c','t','a','c','d'],['c','c','c','c','a']]
s = input()
cnt = 0
for inner in arr:
    cnt += inner.count(s)
if cnt >= 7: print("세상에")
elif cnt >=5 : print("와우")
elif cnt >=3 :print("이야")
else:print("이런")