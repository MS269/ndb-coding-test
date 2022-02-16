from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, breaked = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][breaked]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][breaked] == 0:
                q.append((nx, ny, breaked))
                visited[nx][ny][breaked] = visited[x][y][breaked] + 1

            if graph[nx][ny] == 1 and breaked == 0:
                q.append((nx, ny, breaked + 1))
                visited[nx][ny][breaked + 1] = visited[x][y][breaked] + 1

    return -1


print(bfs())
