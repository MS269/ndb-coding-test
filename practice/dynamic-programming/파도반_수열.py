dp = [0, 1, 1, 1]
for i in range(4, 101):
    dp.append(dp[i - 2] + dp[i - 3])

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
