# union find 자료구조 - 각각의 독립된 데이터를 그룹화 할때

# 1. 이때 그래프에서 cycle 발생 여부를 체크할 수 있다
# 2. 최소신장 트리 :

arr = [0] *200
rank = [0] * 200    # 효율성 증대 (그룹화가 될때 작은 그룹이 큰 그룹 밑으로 갈 수 있도록 체크)
def findboss(member):
    if arr[ord(member)] ==0 :
        return member

    ret = findboss(arr[ord(member)])
    # 매번 타고 들어가는것 없이 보스를 갱신 해주는 코드
    arr[ord(member)] = ret
    return ret


def Union(a,b):
    global arr
    fa, fb = findboss(a),findboss(b)

    # if rank[ord(boss_a)] > rank[ord(boss_b)]:
    #     arr[ord(boss_b)]=boss_a
    # elif rank[ord(boss_a)] < rank[ord(boss_b)]:
    #     arr[ord(boss_a)]= boss_b
    # else:
    #     arr[ord(boss_b)]=boss_a
    #     rank[ord(boss_a)]+=1


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
# union find 자료구조 - 각각의 독립된 데이터를 그룹화 할때

arr = [0] * 200
rank = [0] * 200


def findboss(member):
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret  # 경로단축
    return ret


def Union(a, b):
    global arr
    boss_a, boss_b = findboss(a), findboss(b)
    if boss_a == boss_b:
        return
    arr[ord(boss_b)] = boss_a



Union('A', 'B')
Union('D', 'E')
Union('B', 'E')
Union('B', 'D')
Union('F', 'E')

y, x = input().split()
if findboss(y) == findboss(x):
    print("같은그룹")
else:
    print('다른그룹')
