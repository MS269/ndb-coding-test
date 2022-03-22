from collections import deque
from itertools import combinations


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)

wall_cnt = 0
starts = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            wall_cnt += 1
        elif graph[i][j] == 2:
            starts.append((i, j))


def bfs(active):
    q = deque()
    visited = [[-1] * n for _ in range(n)]

    for x, y in active:
        q.append((x, y))
        visited[x][y] = 0

    max_sec = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 1 and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

                if graph[nx][ny] == 0:
                    max_sec = max(max_sec, visited[nx][ny])

    if list(sum(visited, [])).count(-1) == wall_cnt:
        ans.append(max_sec)


ans = []
for active in combinations(starts, m):
    bfs(active)

print(min(ans) if ans else -1)
