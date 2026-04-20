arr = [4,2,5,1,6,7,3]
a, b = input().split()
num1, num2 = ord(a)-ord("A"), ord(b)-ord("A")
if num1 > num2 : num1,num2=num2,num1
print(sum(arr[num1+1:num2]))