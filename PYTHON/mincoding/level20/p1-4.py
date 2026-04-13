def main():
    num = int(input())
    abc(num)
cnt = 0
def abc(num):
    global cnt
    if cnt > 3:
        return
    else:
        cnt += 1
        abc(num+2) 
        print(num, end=' ')       
        return num
main()