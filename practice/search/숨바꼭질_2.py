from collections import deque


n, k = map(int, input().split())

q = deque([n])
visited = [[-1, 0] for _ in range(100001)]
visited[n][0] = 0
visited[n][1] = 1

while q:
    x = q.popleft()

    for nx in (x - 1, x + 1, 2 * x):
        if 0 <= nx < 100001:
            if visited[nx][0] == -1:
                visited[nx][0] = visited[x][0] + 1
                visited[nx][1] = visited[x][1]
                q.append(nx)
            elif visited[nx][0] == visited[x][0] + 1:
                visited[nx][1] += visited[x][1]

print(visited[k][0])
print(visited[k][1])
