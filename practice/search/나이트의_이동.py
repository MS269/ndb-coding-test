from collections import deque

dx = (1, 2, 2, 1, -1, -2, -2, -1)
dy = (2, 1, -1, -2, -2, -1, 1, 2)

for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    q = deque([(start_x, start_y)])
    graph = [[0] * n for _ in range(n)]

    while q:
        x, y = q.popleft()

        if x == goal_x and y == goal_y:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    print(graph[goal_x][goal_y])
