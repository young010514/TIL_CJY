def main():
    aToZ()
def aToZ():
    data = input()
    a, z = ord("A"), ord("Z")
    s = ord(data)
    if s - a > z-s:print("Z")
    else:print("A")
main()