from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs():
    q = deque([(0, 0)])
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 0
                visited[nx][ny] = True
                cnt += 1

    cnts.append(cnt)


hours = 0
cnts = []
while True:
    visited = [[False] * m for _ in range(n)]

    bfs()

    if cnts[hours] == 0:
        break

    hours += 1

print(hours)
print(cnts[-2])
