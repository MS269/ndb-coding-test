n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            ans += 1
            for k in range(3):
                for l in range(3):
                    a[i + k][j + l] = 1 - a[i + k][j + l]

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            ans = -1

print(ans)
