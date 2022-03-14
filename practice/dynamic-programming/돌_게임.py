n = int(input())

dp = [False, True, False, True]
for i in range(4, n + 1):
    if dp[i - 1] or dp[i - 3]:
        dp.append(False)
    else:
        dp.append(True)

print("SK" if dp[n] else "CY")
