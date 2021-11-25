n = int(input())
foods = list(map(int, input().split()))

# dp 테이블
dp = [0] * n

# dp
dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + foods[i])

print(dp[n - 1])
