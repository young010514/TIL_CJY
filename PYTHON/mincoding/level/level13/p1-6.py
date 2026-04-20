arr = [[4,5,6,1,3,1],[2,1,3,6,3,6]]
def input1():
    return list(map(int,input().split()))

def process(nums):
    result = []
    for n in nums:
        cnt = 0
        for inner in arr:
            cnt += inner.count(n)
        result.append(cnt)
    return nums + result
def output1(data):
    for x in range(3):
        print(f"{data[x]}={data[3+x]}개")
def main():
    output1(process(input1()))
    
main()