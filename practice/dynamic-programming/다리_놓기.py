dp = [[0] * 31 for _ in range(31)]
for i in range(31):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = 1
        elif j == i:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(dp[m][n])
