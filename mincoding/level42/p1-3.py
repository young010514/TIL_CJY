Min = 30
lst= ['BTS','SBS','BS','CBS','SES']
input_st = input()
def dfs(path):
    global Min
    if len(''.join(path)) >= len(input_st) :
        if  ''.join(path) == input_st and Min > len(path):
            Min = len(path)
        return
    for i in lst:
        path.append(i)
        dfs(path)
        path.pop()
dfs([])
print(Min)