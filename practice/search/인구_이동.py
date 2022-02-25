from collections import deque


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

ans = 0
while True:
    q = deque()
    visited = [[False] * n for _ in range(n)]
    is_moved = False

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            q.append((i, j))
            visited[i][j] = True

            union = [(i, j)]
            while q:
                x, y = q.popleft()

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        union.append((nx, ny))

            if len(union) > 1:
                is_moved = True

                population = sum(graph[x][y] for x, y in union) // len(union)
                for x, y in union:
                    graph[x][y] = population

    if not is_moved:
        break

    ans += 1

print(ans)
