n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
dx, dy = (1, 0), (0, 1)


def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1

    if visited[x][y] == -1:
        visited[x][y] = 0

        for i in range(2):
            nx, ny = x + dx[i] * graph[x][y], y + dy[i] * graph[x][y]

            if 0 <= nx < n and 0 <= ny < n:
                visited[x][y] += dfs(nx, ny)

    return visited[x][y]


print(dfs(0, 0))
