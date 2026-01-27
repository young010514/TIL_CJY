arr =[['A','D','F'],['Q','W','E'],['Z','X','C']]
def main():
    x,y = find(input())
    print(f'{x},{y}')
def find(s):
    for x in range(3):
        for y in range(3):
            if arr[x][y] == s:
                return x,y
main()