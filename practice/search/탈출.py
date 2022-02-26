from collections import deque


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)

q = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == "*":
            q.append((i, j))
        elif graph[i][j] == "S":
            q.appendleft((i, j))
        elif graph[i][j] == "D":
            tx, ty = i, j

while q:
    x, y = q.popleft()

    if graph[tx][ty] == "S":
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if graph[nx][ny] == "*" or graph[nx][ny] == "X":
            continue

        if graph[x][y] == "S" and not graph[nx][ny] == "S":
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            graph[nx][ny] = "S"
        elif graph[x][y] == "*" and not graph[nx][ny] == "D":
            q.append((nx, ny))
            graph[nx][ny] = "*"

print(visited[tx][ty] if visited[tx][ty] > 0 else "KAKTUS")
