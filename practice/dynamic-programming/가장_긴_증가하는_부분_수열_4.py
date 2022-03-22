n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

subsequence = []
order = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == order:
        subsequence.append(a[i])
        order -= 1

print(max(dp))
print(*subsequence[::-1])
