#Problem3
def find_majority(ar, n):
    for i in ar:
        if ar.count(i) > n // 2:
            return i
    return -1

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(find_majority(ar, n))