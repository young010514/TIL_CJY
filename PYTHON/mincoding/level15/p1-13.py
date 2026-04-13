arr = [list('DATAW'), list('BBQK')]
n = int(input())
if n % 2 == 1:
    arr[0].sort()
else:arr[1].sort()
print(''.join(arr[0]))
print(''.join(arr[1]))