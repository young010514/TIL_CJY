# DAT -> 누적합 -> 값넣기

n = 10
lst = [7,5,7,3,9,1,7,2,2,3,8,3,4,9,3,7]

# print(len(lst)) # 16

dat_lst = [0]*n
for i in lst:
    dat_lst[i] += 1
nu_lst = [0] *n

# 누적합 구하기
for i in range(n):
    nu_lst[i] = sum(dat_lst[:i+1])

# print(nu_lst) #[0, 1, 3, 7, 8, 9, 9, 13, 14, 16]
new_lst = [0] * nu_lst[-1]
for i in lst:
    nu_lst[i] -= 1
    new_lst[nu_lst[i]] = i
print(new_lst)



# 3 8 5 2 5 7 2 4 입력시 counting sort
# n개의 숫자 입력받은후 O(n)의 속도로 정렬하기 ( 입력값은 1<= 입력값 <= 9 가정하고 문제풀이 )
n=int(input())
a=list(map(int,input().split()))
bucket=[0]*10
# DAT 구성하기
for i in a:
    bucket[i]+=1

# 누적합 구하기
for i in range(1,len(bucket)):
    bucket[i]+=bucket[i-1]

# 값넣기
result=[0]*n
for i in range(n):
    bucket[a[i]]-=1  # 버켓의 값 하나 뺴주고
    index=bucket[a[i]] # result 배열의 몇번 인덱스에 값 넣을지 확인후
    result[index]=a[i] # result 배열에 원본 값 넣기

print(*result)
