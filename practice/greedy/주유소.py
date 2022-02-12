n = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
cost = costs[0]
for i in range(n - 1):
    cost = min(cost, costs[i])
    ans += cost * dists[i]

print(ans)
