#Problem1

def arrange(ar, n):
    tem1 = [i for i in ar if i < 0]
    tem2 = [i for i in ar if i not in tem1]
    res = tem1 + tem2
    return " ".join(str(i) for i in res)

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(arrange(ar, n))