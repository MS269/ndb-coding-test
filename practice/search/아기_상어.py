from collections import deque


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 2
            sx, sy = i, j
            break


def bfs(x, y):
    q = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    eaten = []

    while q:
        x, y, c = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] > graph[sx][sy] or visited[nx][ny]:
                continue

            if 0 < graph[nx][ny] < graph[sx][sy]:
                eaten.append((nx, ny, c + 1))

            q.append((nx, ny, c + 1))
            visited[nx][ny] = True

    if not eaten:
        return (-1, -1, -1)

    eaten.sort(key=lambda x: (x[2], x[0], x[1]))
    return eaten[0]


ans = 0
cnt = 0
while True:
    nx, ny, c = bfs(sx, sy)

    if nx == -1 or ny == -1 or c == -1:
        break

    graph[nx][ny] = graph[sx][sy]
    graph[sx][sy] = 0
    sx, sy = nx, ny
    ans += c
    cnt += 1

    if cnt == graph[sx][sy]:
        graph[sx][sy] += 1
        cnt = 0

print(ans)
