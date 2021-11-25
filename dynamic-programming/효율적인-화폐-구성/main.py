n, m = map(int, input().split())
currencies = [int(input()) for _ in range(n)]

dp = [10001] * (m + 1)

dp[0] = 0
for currency in currencies:
    for i in range(currency, m + 1):
        if dp[i - currency] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
            dp[i] = min(dp[i], dp[i - currency] + 1)

# 계산된 결과 출력
if dp[m] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(dp[m])
