def main():
    x, y = map(int, input().split())
    return x, y

def BBQ(x):
    a, b= x[0], x[1]
    print(f"합:{a + b}\n차:{a - b}\n곱:{a * b}\n몫:{a // b}")
BBQ(main())