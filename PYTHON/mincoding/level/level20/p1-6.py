def abc(num, max):
    if num == max :
        print(num,end=' ')
        return
    print(num,end=' ')
    abc(num +1, max)
    print(num, end=' ')


a,b= map(int,input().split())
abc(a,b)