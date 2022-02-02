from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    ret = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] or graph[nx][ny] == 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = True
            ret += 1

    return ret


tot = 0
counters = []

for i in range(n):
    for j in range(n):
        if visited[i][j] or graph[i][j] == 0:
            continue

        cnt = bfs(i, j)
        tot += 1
        counters.append(cnt)

counters.sort()
print(tot, *counters, sep="\n")
