for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    a.sort()

    m = a[0][1]
    ans = 1

    for i in range(1, n):
        if a[i][1] < m:
            m = a[i][1]
            ans += 1

    print(ans)
