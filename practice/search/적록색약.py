import sys


def dfs(x, y, c):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not visited[nx][ny] and graph[nx][ny] == c:
            dfs(nx, ny, c)


sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(input()) for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

visited = [[False] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

visited = [[False] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            cnt2 += 1

print(cnt1, cnt2)
