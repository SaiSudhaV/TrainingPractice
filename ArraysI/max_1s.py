#1. Given a binary array nums, return the maximum number of consecutive 1's in the array.

def max_consecutive_1s(ar, n):
    res, count = 0, 0
    for i in range(n):
        if ar[i] == 1:
            count += 1
            res = max(res, count)
        else:
            count = 0
    return res

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    print(max_consecutive_1s(ar, len(ar)))