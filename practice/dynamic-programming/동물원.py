n = int(input())

dp = [[0, 0, 0], [1, 1, 1]]
for i in range(2, n + 1):
    dp.append([sum(dp[i - 1]) % 9901,
              (dp[i - 1][0] + dp[i - 1][2]) % 9901,
              (dp[i - 1][0] + dp[i - 1][1]) % 9901])

print(sum(dp[n]) % 9901)
