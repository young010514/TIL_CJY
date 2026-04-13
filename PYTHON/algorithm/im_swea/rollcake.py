import  sys
sys.stdin = open("input_cake.txt","r")

n = int(input())
p_num = int(input())
p_lst = [tuple(map(int,input().split())) for _ in range(p_num)]
Max = -1

for idx, ij in enumerate(p_lst):
    if Max < ij[1]-ij[0] :
        Max = ij[1]-ij[0]
        expect = idx

cake = [-1] * n

for idx, (i,j) in enumerate(p_lst):
    # print(idx, i,j)
    for x in range(i-1,j):
        if cake[x] != -1 : continue
        else : cake[x] = idx
cnt_lst = [0] * p_num
for i in range(p_num) :
    cnt_lst[i] = cake.count(i)

# 0부터 인덱스 시작하니까
print(expect + 1)
print(cnt_lst.index(max(cnt_lst)) + 1)
