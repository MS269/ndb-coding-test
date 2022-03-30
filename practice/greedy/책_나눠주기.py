for _ in range(int(input())):
    n, m = map(int, input().split())
    ranges = [list(map(int, input().split())) for _ in range(m)]

    ranges.sort(key=lambda x: x[1])

    ans = 0
    books = [False] * (n + 1)
    for a, b in ranges:
        for i in range(a, b + 1):
            if not books[i]:
                books[i] = True
                ans += 1
                break

    print(ans)
