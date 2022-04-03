from collections import deque


s = int(input())
visited = [[-1] * (s + 1) for _ in range(s + 1)]


def bfs():
    q = deque([(1, 0)])
    visited[1][0] = 0

    while q:
        x, y = q.popleft()

        if visited[x][x] == -1:
            q.append((x, x))
            visited[x][x] = visited[x][y] + 1

        if x + y <= s and visited[x + y][y] == -1:
            q.append((x + y, y))
            visited[x + y][y] = visited[x][y] + 1

        if x - 1 >= 0 and visited[x - 1][y] == -1:
            q.append((x - 1, y))
            visited[x - 1][y] = visited[x][y] + 1


bfs()

ans = visited[s][1]
for i in visited[s]:
    if i != -1:
        ans = min(ans, i)

print(ans)
