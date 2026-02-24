# 글로벌 변수(전역변수)의 값을 다른 함수에서 바꿀 시에는 반드시 global을 명시해야함


def kfc():
    print(aa, bb, 'kfc')
    aa += 1  # global을 명시하지 않은 상태에서 값을 변경하려는 시도 
            #  즉,메모리 값을 변경하려는 시도를 진행하는 순간부터 error 발생
            # 근데 왜 이건 위의 print도 안되는건지 모르겠음
    bb +=1 
    print(aa, bb, 'kfc')
    
def test():
    global aa, bb
    aa= 3
    bb =5
    print(aa, bb,' test')

test()
kfc()


# 함수 호출 시 컴파일 단계에서 aa,bb 를 local로 처리하고,

# 실행 단계에서 print(aa, bb)에서 local 변수를 찾지만, 해당 함수 내에는 지역변수 선언이 되어있지 않기 때문에 

# 4번째 줄에서부터 오류가 난다.

# 추가 

# 5, 6번 줄을 제거할 시 함수 내 컴파일 단계에서 aa,bb를 local로 처리하지 않으니

# 4번째 줄 print(aa,bb)할때 local에서 aa,bb를 찾고, 없으니 전역변수로 찾아서 print 가능