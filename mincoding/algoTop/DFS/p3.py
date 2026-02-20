# inorder, preorder ,postorder
n = int(input())
lst =[list(map(int,input().split())) for _ in range(n)]
lst1 = [0] * 1001
for i in range(n):
    lst1[lst[i][0]] = [lst[i][1], lst[i][2]]
nds = [0] * (n+1)
# find root
for i in range(n):
    for x in range(3):
        if lst[i][x] ==-1:continue
        nds[lst[i][x]] += 1
root = nds.index(1)

def inorder(node):
    if node != -1:
        left = lst1[node][0]
        right = lst1[node][1]
        inorder(left)
        print(node,end=' ')
        inorder(right)

def preorder(node):
    if node != -1:
        left = lst1[node][0]
        right = lst1[node][1]
        print(node,end=' ')
        preorder(left)
        preorder(right)

def postorder(node):
    if node != -1:
        left = lst1[node][0]
        right = lst1[node][1]
        postorder(left)
        postorder(right)
        print(node,end=' ')
inorder(root)
print()
preorder(root)
print()
postorder(root)