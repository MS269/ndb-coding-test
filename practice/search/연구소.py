from collections import deque
from copy import deepcopy


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs():
    q = deque()
    temp_graph = deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if temp_graph[nx][ny] != 0:
                continue

            temp_graph[nx][ny] = 2
            q.append((nx, ny))

    ret = 0

    for i in temp_graph:
        ret += i.count(0)

    return ret


def wall(cnt):
    if cnt == 3:
        global ans
        ans = max(ans, bfs())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0


ans = 0

wall(0)

print(ans)
