arr = ['M','T','K','C']

def isExist(arr, x):
    result = False
    for i in arr:
        if i == x :
            result = True
    if result :
        print("발견")
    else:print("미발견")
x =input()
isExist(arr,x)