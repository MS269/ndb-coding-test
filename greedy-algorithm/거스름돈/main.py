n = 1260
cnt = 0
coin_types = [500, 100, 50, 10]

# 큰 단위부터 거슬러 주기
for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)
