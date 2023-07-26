def KhoangCachGiuaNhieuDiem(n):
    r1 = r2 = s1 = s2 = 0
    for i in range(n):
        x, y = map(int, input().split())
        s1 += x
        r1 += (n + 1) * x * x - 2 * x * s1
        s2 += y
        r2 += (n + 1) * y * y - 2 * y * s2
    t = r1 + r2
    return t

n = int(input())
print(KhoangCachGiuaNhieuDiem(n))