from collections import deque


for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    w = int(input())

    q = deque()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = d[i]

    while q:
        v = q.popleft()

        for i in graph[v]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[v] + d[i])

            if in_degree[i] == 0:
                q.append(i)

    print(dp[w])
