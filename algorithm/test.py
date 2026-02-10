y = int(input())
def check(num):
    if num % 4 ==0 :
        if num % 100 == 0 and num % 400 != 0:
            return "false"
        else:return "true"
    return "false"
print(check(y))