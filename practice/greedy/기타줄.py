n, m = map(int, input().split())

min_package = 1000
min_piece = 1000
for _ in range(m):
    a, b = map(int, input().split())
    min_package = min(min_package, a)
    min_piece = min(min_piece, b)

ans = min(min_package, min_piece * 6) * (n // 6) + \
    min(min_package, min_piece * (n % 6))
print(ans)
