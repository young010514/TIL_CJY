id = "qlqlaqkq"
pw = "tkaruqtkf"

def main(i,p):
    if i == id and p == pw:
        return "LOGIN"
    else:return "INVALID"
i=input().strip()
p = input().strip()
print(main(i,p))