from collections import deque
from copy import deepcopy
from sys import maxsize


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def get_waterside(x, y):
    q = deque([(x, y)])
    waterside = deque()
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif graph[nx][ny] == 0:
                waterside.append((nx, ny, 1))

    return waterside


def get_min_len(q):
    min_len = maxsize
    visited_water = deepcopy(visited)

    while q:
        x, y, c = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited_water[nx][ny]:
                continue

            if graph[nx][ny] == 0:
                q.append((nx, ny, c + 1))
                visited_water[nx][ny] = True
            elif graph[nx][ny] == 1:
                min_len = min(min_len, c)

    return min_len


ans = maxsize
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            waterside = get_waterside(i, j)
            ans = min(ans, get_min_len(waterside))

print(ans)
