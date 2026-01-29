# try except 문을 알고리즘 풀때 스지 마세요  .... is else
# web api 요청 -- 응답을 잘 받으면 or 응답이 안오면 이렇게 처리해라 ...등을 표현할때 

# try : 
#     num = input() #aa
#     print(int(num))
# except:
#     print("숫자입력하세요")



try : 
    age = int(input("나이를 입력하세요"))
except:
    print("입력이 정확하지 않습니다")


else:       # except로 빠져나오면 이 구문은 작동하지 않는다.
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다")

finally:  # except를 해도 작동하는 코드
    print('ㅅㄱ')