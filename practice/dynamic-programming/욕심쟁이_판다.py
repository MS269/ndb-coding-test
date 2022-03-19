import sys


sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)
