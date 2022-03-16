from sys import maxsize


for _ in range(int(input())):
    k = int(input())
    a = list(map(int, input().split()))

    dp = [[0] * k for _ in range(k)]
    for d in range(1, k):
        for i in range(k - d):
            j = i + d
            dp[i][j] = maxsize
            temp = sum(a[i: j + 1])
            for m in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j] + temp)

    print(dp[0][-1])
