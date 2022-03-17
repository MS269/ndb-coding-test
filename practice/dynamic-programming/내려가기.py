n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_temp = [0] * 3
min_temp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())

    max_temp[0] = a + max(max_dp[0], max_dp[1])
    min_temp[0] = a + min(min_dp[0], min_dp[1])

    max_temp[1] = b + max(max_dp)
    min_temp[1] = b + min(min_dp)

    max_temp[2] = c + max(max_dp[1], max_dp[2])
    min_temp[2] = c + min(min_dp[1], min_dp[2])

    for j in range(3):
        max_dp[j] = max_temp[j]
        min_dp[j] = min_temp[j]

print(max(max_dp), min(min_dp))
