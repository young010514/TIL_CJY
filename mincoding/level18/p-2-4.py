lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
cnt = 0
for i in range(len(lst1)):
    if lst1[i] == 1 and lst2[i] == 1: cnt +=1 
print(f"{cnt}개")