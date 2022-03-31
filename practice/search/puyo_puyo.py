from collections import deque


graph = [list(input()) for _ in range(12)]
dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)


def bfs(x, y):
    global broken

    q = deque([(x, y)])
    visited = [[False] * 6 for _ in range(12)]
    visited[x][y] = True
    puyo = [(x, y)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    puyo.append((nx, ny))

    if len(puyo) >= 4:
        broken = True

        while puyo:
            x, y = puyo.pop()
            graph[x][y] = "."


ans = 0
while True:
    broken = False

    for i in range(12):
        for j in range(6):
            if graph[i][j] != ".":
                bfs(i, j)

    if not broken:
        break

    ans += 1

    for j in range(6):
        for i in range(11, -1, -1):
            if graph[i][j] == ".":
                for k in range(i - 1, -1, -1):
                    if graph[k][j] != ".":
                        graph[i][j] = graph[k][j]
                        graph[k][j] = "."
                        break

print(ans)
