def checkChar(char):
    if char == char.upper() : print('대', end='')
    else : print('소',end='')


arr1 = input().split()
for i in arr1:
    checkChar(i)