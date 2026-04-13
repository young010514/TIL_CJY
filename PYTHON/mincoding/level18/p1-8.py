train = [3,7,6,4,2,9,1,7]
team = list(map(int,input().split()))
print(f'{train.index(team[0])}번~{train.index(team[-1])}번 칸')
            