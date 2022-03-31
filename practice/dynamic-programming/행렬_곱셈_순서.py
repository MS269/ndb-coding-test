from sys import maxsize


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(1, n):
    for j in range(n - i):
        dp[j][j + i] = maxsize
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1]
                               [j + i] + a[j][0] * a[k][1] * a[j + i][1])

print(dp[0][-1])
