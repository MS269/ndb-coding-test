n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

a.sort()

dp = [100001] * (k + 1)
dp[0] = 0
for i in range(1, k + 1):
    for j in a:
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[k] if dp[k] != 100001 else -1)
