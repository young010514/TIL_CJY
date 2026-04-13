# 8 스위치 개수
# 0 1 0 1 0 0 0 1 # 스위치 상태 arr
# 2 # 학생수
# 1 3 # 성별, 넘버(기준점)
# 2 3

Switch=int(input())
arr=list(map(int,input().split()))
Students=int(input())

for i in range(Students):
    gender,number=map(int,input().split())
    number-=1 # 배열은 0번 인덱스 부터 시작하므로 숫자를 1감소시킴

    if gender==1:
        for i in range(number,Switch,number+1):
            arr[i]=1-arr[i]
    else:
        for i in range(Switch//2):
            right=number+i
            left=number-i
            if right==Switch or left<0: # 배열 범위 체크
                break
            if arr[right]==arr[left]:
                arr[right]=1-arr[right]
                arr[left]=arr[right]
            else:  # 왼쪽 오른쪽 값이 다르면 꺼버리기
                break

for i in range(Switch):
    print(arr[i],end=' ')
    if (i+1)%20==0:
        print()