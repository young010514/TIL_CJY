def main():
    a, b = map(int,input().split())
    s = sum1(a,b)
    c = comp1(a,b)
    print1(s, c)

def sum1(x,y):
    return x+y
def comp1(x,y):
    return abs(x-y)
def print1(x,y):
    print(f'합:{x}\n차:{y}')

main()