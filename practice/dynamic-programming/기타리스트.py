n, s, m = map(int, input().split())
v = [0] + list(map(int, input().split()))

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][s] = True
for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j]:
            if j + v[i] <= m:
                dp[i][j + v[i]] = True
            if j - v[i] >= 0:
                dp[i][j - v[i]] = True

ans = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        ans = i
        break

print(ans)
