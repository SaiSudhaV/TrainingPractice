#Problem2

def arrange(ar, n):
    neg = [i for i in ar if i < 0]
    pos = [i for i in ar if i not in neg]
    res, j, k = [], 0, 0
    for i in range(0, n):
        if i % 2 == 0:
            res.append(pos[j])
            j += 1
        else:
            res.append(neg[k])
            k += 1
    return " ".join(str(i) for i in res)

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(arrange(ar, n))