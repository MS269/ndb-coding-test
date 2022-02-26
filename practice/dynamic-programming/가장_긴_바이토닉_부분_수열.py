n = int(input())
a = list(map(int, input().split()))

inc_dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

a.reverse()
dec_dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

dp = [inc_dp[i] + dec_dp[-(i + 1)] - 1 for i in range(n)]

print(max(dp))
