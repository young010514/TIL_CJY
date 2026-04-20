num = int(input())
a = (num // 1000)%10
b = (num // 100)%10
c = num // 10 %10
d = num % 10
print(f'숫자{a}')
print(f'숫자{b}')
print(f'숫자{c}')
print(f'숫자{d}')