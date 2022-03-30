from collections import deque


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
hx, hy = (1, 2, 2, 1, -1, -2, -2, -1), (2, 1, -1, -2, -2, -1, 1, 2)
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs():
    q = deque([(0, 0, k)])
    visited[0][0][k] = 0

    while q:
        x, y, c = q.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][c]

        if c > 0:
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 0 and visited[nx][ny][c - 1] == -1:
                        q.append((nx, ny, c - 1))
                        visited[nx][ny][c - 1] = visited[x][y][c] + 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 0 and visited[nx][ny][c] == -1:
                    q.append((nx, ny, c))
                    visited[nx][ny][c] = visited[x][y][c] + 1

    return -1


print(bfs())
