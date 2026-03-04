# union find 자료구조 - 각각의 독립된 데이터를 그룹화 할때

# 1. 이때 그래프에서 cycle 발생 여부를 체크할 수 있다
# 2. 최소신장 트리 :

arr = [0] *200
def findboss(member):
    if arr[ord(member)] ==0 :
        return member

    ret = findboss(arr[ord(member)])
    return ret


def Union(a,b):
    global arr
    fa, fb = findboss(a),findboss(b)

    if fa == fb : return        # 이미 보스가 같은경우
    arr[ord(fb)] = fa

Union("A","B")
Union("D","E")
Union("B","E")
Union("B","D")

a,b = input().split()
if findboss(a) == findboss(b):
    print("boss same")
else: print("dif group")
