from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    area = 0

    while q:
        x, y = q.popleft()
        area += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return area


cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)
