import sys


sys.setrecursionlimit(1000000)
t = int(input())
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny] or graph[nx][ny] == 0:
            continue

        dfs(nx, ny)


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    ans = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 or visited[i][j]:
                continue

            dfs(i, j)
            ans += 1

    print(ans)
