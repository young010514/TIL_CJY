win = [[3,5,1],[4,2,6]]
people = list(map(int,input().split()))
for i in people:
    result = "불합격"
    for x in win:
        if i in x : result = "합격"
    print(f"{i}번 {result}")