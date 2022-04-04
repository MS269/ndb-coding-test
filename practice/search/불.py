from collections import deque


dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)


def bfs():
    cnt = 0

    while q:
        cnt += 1

        while fire and fire[0][2] < cnt:
            x, y, c = fire.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == ".":
                        fire.append((nx, ny, c + 1))
                        graph[nx][ny] = "*"

        while q and q[0][2] < cnt:
            x, y, c = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == "." and not visited[nx][ny]:
                        q.append((nx, ny, c + 1))
                        visited[nx][ny] = True
                else:
                    return cnt

    return "IMPOSSIBLE"


for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    q = deque()
    fire = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "@":
                q.append((i, j, 0))
                visited[i][j] = True
            elif graph[i][j] == "*":
                fire.append((i, j, 0))

    print(bfs())
