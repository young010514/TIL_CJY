# Greatest Common divisor (GCD - 최대 공약수)



# answer = 0
# a,b = map(int,input().split())
# while b:
#     test= a
#     a = b
#     b = test % a
# print(a)

# 최대 공약수 - 유클리드 호제법
# 최소 공배수 - a,b -> lcm = gcd * (a / gcd ) * (b / gcd)

# =============================================
# prime number (소수) 구하기
# 소수 = 1과 자기 자신으로만 나눌 수 있는 수

# 2부터 차례대로 확인하는 방법
# 20 입력 시 20보다 작은 소수를 출력하기

# 비추천!
# n = int(input())
# ans = []    # n보다 작은 소수를 저장할 리스트
# for i in range(2,n+1):
#     flag = 0
#     for j in range(2,i):
#         if i % j == 0 :
#             flag=  1
#             break
#     if flag ==0:
#         ans.append(i)
# print(*ans)

# 에라토스테네스의 체 라는 알고리즘을 활용해서 조금 더 빠른 속도로 소수들 구하기

# n = int(input())
# ans = [0] * (n+1)
# ans[0],ans[1] = 1,1
# idx = 2
# while idx**2 < n:
#     d = 2
#     while 1:
#         if idx * d > n : break
#         ans[idx * d] = 1
#         d += 1
#
#     idx += 1
#
# for i in range(n+1):
#     if ans[i] ==0 :print(i,end=' ')



# a= int(input())
# check = [0] * (a+1)
# end = int(a**0.5)
# for i in range(2,end+1):
#     if check[i]== 1 : continue
#     for j in range(i+i, a+1, i):
#         check[j] = 1
#
# for i in range(2,a+1):
#     if check[i] == 0 : print(i,end=' ')


# =======================================
# sliding window = 빠른 탐색
# n,m= map(int,input().split())
# arr = list(map(int,input().split()))
# Sum = 0
# # 첫 m개의 구간의 합부터 구하기
# for i in range(m):
#     Sum += arr[i]
# Max = Sum
# for i in range(n-m):
#     Sum += arr[i+m]
#     Sum -= arr[i]
#     if Sum > Max:
#         Max = Sum
# print(Max)


# =====================================

n,m = map(int,input().split())
arr = list(map(int,input().split()))
lft, rgt = 0,0
Sum = 0
cnt = 0
while lft < n:
    if Sum >= m or rgt >= n-1 :
        Sum -= arr[lft]
        lft += 1
    elif Sum < m:
        Sum += arr[rgt]
        rgt += 1
        continue

    if Sum == m : cnt += 1

print(cnt)























