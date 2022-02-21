for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    dp = [[]]
    dp.append([a[1], b[1]])
    if n > 1:
        dp.append([a[2] + b[1], b[2] + a[1]])
    for i in range(3, n + 1):
        dp.append([a[i] + max(dp[i - 1][1], dp[i - 2][1]),
                  b[i] + max(dp[i - 1][0], dp[i - 2][0])])

    print(max(dp[n]))
