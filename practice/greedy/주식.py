for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    max_stock = 0
    for stock in reversed(a):
        if stock > max_stock:
            max_stock = stock
        else:
            ans += max_stock - stock

    print(ans)
