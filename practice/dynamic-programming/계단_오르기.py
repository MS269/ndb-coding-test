n = int(input())
a = [0]
for _ in range(n):
    a.append(int(input()))


def solve(n):
    if n == 1:
        return a[1]

    if n == 2:
        return a[1] + a[2]

    dp = [[0, 0], [a[1], 0], [a[1] + a[2], a[2]]]
    for i in range(3, n + 1):
        step1 = dp[i - 1][1] + a[i]
        step2 = max(dp[i - 2]) + a[i]
        dp.append([step1, step2])
    return max(dp[n])


print(solve(n))
