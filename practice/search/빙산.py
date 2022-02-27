from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    melting_list = []

    while q:
        x, y = q.popleft()
        melting_cnt = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            if graph[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            else:
                melting_cnt += 1

        if melting_cnt:
            melting_list.append((x, y, melting_cnt))

    return melting_list


ans = 0
while True:
    visited = [[False] * m for _ in range(n)]
    part_cnt = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] != 0 and not visited[i][j]:
                part_cnt += 1
                melting_list = bfs(i, j)

                for x, y, c in melting_list:
                    graph[x][y] = max(0, graph[x][y] - c)

    if part_cnt == 0:
        ans = 0
        break
    if part_cnt >= 2:
        break

    ans += 1

print(ans)
