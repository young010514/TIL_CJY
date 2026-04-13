import sys
sys.stdin = open("input_scan.txt")

hex_to_bin = {
    '0':'0000','1':'0001','2':'0010','3':'0011',
    '4':'0100','5':'0101','6':'0110','7':'0111',
    '8':'1000','9':'1001','A':'1010','B':'1011',
    'C':'1100','D':'1101','E':'1110','F':'1111'
}

code = {
    (3,2,1):0,
    (2,2,1):1,
    (2,1,2):2,
    (1,4,1):3,
    (1,3,2):4,
    (1,2,3):5,
    (1,1,4):6,
    (1,3,1):7,
    (1,2,1):8,
    (3,1,1):9
}

T = int(input())

for tc in range(1, T+1):

    N, M = map(int,input().split())
    arr = [input().strip() for _ in range(N)]

    visited = set()
    answer = 0

    for row in arr:

        binary = ''.join(hex_to_bin[c] for c in row)

        idx = len(binary)-1

        while idx >= 55:

            if binary[idx] == '1':

                c2 = c3 = c4 = 0

                while binary[idx] == '1':
                    c2 += 1
                    idx -= 1

                while binary[idx] == '0':
                    c3 += 1
                    idx -= 1

                while binary[idx] == '1':
                    c4 += 1
                    idx -= 1

                k = min(c2,c3,c4)

                pattern = (c4//k, c3//k, c2//k)

                if pattern in code:

                    nums = []
                    nums.append(code[pattern])

                    for _ in range(7):

                        c2=c3=c4=0

                        while binary[idx] == '1':
                            c2+=1; idx-=1
                        while binary[idx] == '0':
                            c3+=1; idx-=1
                        while binary[idx] == '1':
                            c4+=1; idx-=1

                        k = min(c2,c3,c4)
                        pattern = (c4//k, c3//k, c2//k)

                        nums.append(code[pattern])

                    nums.reverse()

                    key = tuple(nums)

                    if key not in visited:

                        visited.add(key)

                        odd = nums[0]+nums[2]+nums[4]+nums[6]
                        even = nums[1]+nums[3]+nums[5]

                        if (odd*3 + even + nums[7]) % 10 == 0:
                            answer += sum(nums)

            else:
                idx -= 1

    print(f"#{tc} {answer}")