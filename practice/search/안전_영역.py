import sys


def dfs(x, y, h):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not visited[nx][ny] and graph[nx][ny] > h:
            dfs(nx, ny, h)


sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

ans = 0
for h in range(max(map(max, graph))):
    visited = [[False] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                dfs(i, j, h)
                cnt += 1

    ans = max(ans, cnt)

print(ans)
