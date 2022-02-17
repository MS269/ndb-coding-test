from collections import deque


m, n, k = map(int, input().split())
graph = [[1] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

for _ in range(k):
    bx, by, tx, ty = map(int, input().split())

    for i in range(bx, tx):
        for j in range(by, ty):
            graph[j][i] = 0

areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            q = deque([(i, j)])
            visited[i][j] = True
            area = 1

            while q:
                x, y = q.popleft()

                for l in range(4):
                    nx = x + dx[l]
                    ny = y + dy[l]

                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    if graph[nx][ny] == 1 and visited[nx][ny] == False:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        area += 1

            areas.append(area)

areas.sort()

print(len(areas))
print(*areas)
