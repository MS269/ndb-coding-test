for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    l.sort()

    ans = 0
    for i in range(2, n):
        ans = max(ans, l[i] - l[i - 2])

    print(ans)
