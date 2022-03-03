r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx, dy = (-1, 0, 1), (1, 1, 1)


def dfs(x, y):
    if y == c - 1:
        return True

    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if graph[nx][ny] == "." and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True

    return False


ans = 0
for i in range(r):
    if graph[i][0] == ".":
        visited[i][0] = True
        if dfs(i, 0):
            ans += 1

print(ans)
