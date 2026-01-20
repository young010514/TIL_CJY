arr = ['A','F','G','A','B','C']
a, b = input().split()
if a in arr and b in arr: print("와2개")
elif a in arr or b in arr : print('오1개')
else:print("우0개")