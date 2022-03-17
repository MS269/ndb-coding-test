n = int(input())
a = list(map(int, input().split()))

ans = 0
if n == 1:
    ans = sum(a) - max(a)
else:
    pairs = sorted([min(a[0], a[5]), min(a[1], a[4]), min(a[2], a[3])])

    min1 = pairs[0]
    min2 = pairs[0] + pairs[1]
    min3 = sum(pairs)

    n1 = (n - 2) ** 2 + 4 * (n - 2) * (n - 1)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    ans = n1 * min1 + n2 * min2 + n3 * min3

print(ans)
