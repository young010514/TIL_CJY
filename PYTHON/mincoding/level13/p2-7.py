arr = [['D','A','S'],['Q','W','V'],['R','T','Y']]
def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    Find((x1,y1),(x2,y2))
    
def Find(a,b):
    print(arr[a[0]][a[1]], arr[b[0]][b[1]])
main()