n = int(input())

dp = [0, [0, 1], [1, 0]]
for i in range(3, n + 1):
    dp.append([dp[i - 1][0] + dp[i - 1][1], dp[i - 1][0]])

print(sum(dp[n]))
