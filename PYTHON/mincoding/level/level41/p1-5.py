card = input().split()

path = [''] * len(card)
visited = [0] * len(card)
def abc(level):
    if level == len(card):
        print(''.join(path))
        return
    for i in range(3):
        if visited[i] == 0:
            path[level] = card[i]
            visited[i] = 1
            abc(level+1)
            path[level] = 0
            visited[i] = 0
abc(0)