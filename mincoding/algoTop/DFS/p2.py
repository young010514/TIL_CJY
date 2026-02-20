n,k = map(int,input().split())
s = int(input())
lst = [tuple(map(int,input().split())) for _ in range(k)]
used_pre =[0] * (n+1)
used_post =[0] * (n+1)
def pre_order(node):
    global used_pre
    nds = []
    for i, j in lst:
        if i != node: continue
        nds.append(j)
    nds.sort(reverse=True)
    print(node,end= ' ')
    for x in nds:
        if used_pre[x] == 0:
            used_pre[x] = 1
            pre_order(x)


def post_order(node):
    global used_post
    left,right = 0,0
    nds = []
    for i,j in lst:
        if i != node :continue
        nds.append(j)
    nds.sort(reverse=True)
    for x in nds:
        if used_post[x] == 0:
            used_post[x] =1
            post_order(x)
    print(node,end=' ')

used_post[s],used_pre[s] = 1,1
pre_order(s)
print()
post_order(s)