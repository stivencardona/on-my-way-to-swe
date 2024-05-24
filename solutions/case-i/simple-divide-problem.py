def binary_search(p, q):
    low = 1
    hight = p + 1
    while (hight - low) > 1:
        mid = (low + hight) >> 1
        if q * mid > p:
            hight = mid
        else:
            low = mid
    return low


p = int(input("p: "))
q = int(input("q: "))

ans = binary_search(p, q)
r = p - q * ans
print(f"ans: {ans}, r: {r}")