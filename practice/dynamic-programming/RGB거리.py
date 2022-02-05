n = int(input())
dp = [[], list(map(int, input().split()))]

for i in range(2, n + 1):
    r, g, b = map(int, input().split())

    r = r + min(dp[i-1][1], dp[i-1][2])
    g = g + min(dp[i-1][0], dp[i-1][2])
    b = b + min(dp[i-1][0], dp[i-1][1])

    dp.append([r, g, b])

print(min(dp[n]))
