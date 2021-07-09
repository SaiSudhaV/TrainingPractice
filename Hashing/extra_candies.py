def possible_extra_candies(ar, n):
    tem, res = max(ar), []
    for i in ar:
        if i + n >= tem:
            res.append("true")
        else:
            res.append("false")
    return res

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    n = int(input())
    print(possible_extra_candies(ar, n))