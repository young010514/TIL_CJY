def main():
    lst1 = FindABC(input())
    lst2 = FindABC(input())
    print(f'A:{lst1[0]+lst2[0]}')
    print(f'B:{lst1[1]+lst2[1]}')
    print(f'C:{lst1[2]+lst2[2]}')    

def FindABC(s):
    a,b,c=0,0,0
    for i in list(s):
        if i == "A":a +=1
        elif i == "B" : b +=1
        elif i == "C" : c += 1

    return [a,b,c]
    
main()