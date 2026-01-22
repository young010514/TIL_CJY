def main():
    gop = GOP()
    sum = SUM()
    if gop > sum : print("GOP>SUM")
    elif gop < sum : print("GOP<SUM")
    else : print("GOP==SUM")
def GOP():
    a, b= map(int,input().split())
    return a * b
def SUM():
    a, b= map(int,input().split())
    return a + b
main()