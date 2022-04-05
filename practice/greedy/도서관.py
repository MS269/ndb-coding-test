n, m = map(int, input().split())
a = list(map(int, input().split()))

plus = [i for i in a if i >= 0]
minus = [-i for i in a if i < 0]

plus.sort(reverse=True)
minus.sort(reverse=True)

dist = []

for i in range(0, len(plus), m):
    dist.append(plus[i])

for i in range(0, len(minus), m):
    dist.append(minus[i])

dist.sort()

ans = dist.pop()
ans += sum(dist) * 2

print(ans)
