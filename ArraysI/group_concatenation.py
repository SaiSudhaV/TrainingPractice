# 9. Consider a string, group the similar characters in combinations. Then, concatenate first element and last element alternatively.

# 9. Consider a string, group the similar characters in combinations. Then, concatenate first element and last element alternatively.

def rotation(s, n):
    tem, res = [], ""
    for i in sorted(set(s.lower())):
        comb = [i for i in range(n) if s[i].lower() == s]
        print(comb)
        p = ""
        for i in comb:
            p += s[i]
        tem.append(p)
    m = len(tem)
    for i in range(m // 2):
        res += tem[i] + tem[-(i + 1)]
        if m % 2:
            res += tem[m // 2]
    return res

if __name__ == "__main__":
    s = input()
    print(rotation(s, len(s)))