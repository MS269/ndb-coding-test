dp = [0] * (10 ** 6 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 10 ** 6 + 1):
    dp[i] = sum(dp[i - 3: i]) % 1000000009

for _ in range(int(input())):
    print(dp[int(input())])
