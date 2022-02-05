from collections import deque


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)


def bfs():
    q = deque()

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] != 0:
                continue

            graph[ny][nx] = graph[y][x] + 1
            q.append((nx, ny))

    ret = 0

    for i in graph:
        for j in i:
            if j == 0:
                return -1
            ret = max(ret, j)

    return ret - 1


print(bfs())
