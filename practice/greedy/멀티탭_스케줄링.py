n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
power = []
for i in range(k):
    if a[i] in power:
        continue

    if len(power) < n:
        power.append(a[i])
        continue

    nexts = []
    for j in power:
        try:
            next = a.index(j, i)
        except:
            next = 101

        nexts.append(next)

    ans += 1
    power[nexts.index(max(nexts))] = a[i]

print(ans)
