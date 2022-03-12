n = int(input())
k = int(input())
a = list(map(int, input().split()))

if k >= n:
    print(0)
else:
    a.sort()

    dists = [a[i + 1] - a[i] for i in range(n - 1)]

    dists.sort()

    for _ in range(k - 1):
        dists.pop()

    print(sum(dists))
