def dot_product(v1, v2):
    i = 0
    j = 0
    ans = 0
    while i < len(v1) and j < len(v2):
        (k1, d1) = v1[i]
        (k2, d2) = v2[j]
        if k1 > k2:
            j += 1
            pass
        if k1 < k2:
            i += 1
            pass
        if k1 == k2:
            ans += d1 * d2
            i +=1
            j += 1
    return ans

v1 = [(1, 2), (5, 3), (7, 4), (8, 2)]
v2 = [(1, 2), (2, 3), (7, 4), (9, 5)]

assert dot_product(v1, v2) == 20

print(dot_product(v1, v2))
