n, c = map(int, input().split())
m = int(input())
a = [list(map(int, input().split())) for _ in range(m)]

a.sort(key=lambda x: x[1])

ans = 0
weights = [c] * (n + 1)
for start, end, weight in a:
    load = c

    for j in range(start, end):
        load = min(load, weights[j])

    load = min(load, weight)

    for j in range(start, end):
        weights[j] -= load

    ans += load

print(ans)
