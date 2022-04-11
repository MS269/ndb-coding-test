n, k = map(int, input().split())

ans = 0
while bin(n).count("1") > k:
    ans += 1
    n += 1

print(ans)
