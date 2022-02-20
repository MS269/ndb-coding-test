import sys

sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] < graph[x][y]:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))
