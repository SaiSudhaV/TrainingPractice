#Problem 4

def solve(arr, n):
    count = 0
    res = 0
    for i in arr:
        if(i == 0 and count % 2 != 0):
            continue
        elif (i == 1 and count % 2 == 0):
            continue
        elif (i == count % 2):
            res += 1
            count += 1
    return res

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(solve(ar, n))