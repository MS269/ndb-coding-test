from collections import deque


MAX = 100001

n, k = map(int, input().split())

q = deque([n])
visited = [-1] * MAX
visited[n] = 0
while q:
    x = q.popleft()

    if x == k:
        break

    if 0 < 2 * x < MAX and visited[2 * x] == -1:
        visited[2 * x] = visited[x]
        q.appendleft(2 * x)

    if 0 <= x - 1 < MAX and visited[x - 1] == -1:
        visited[x - 1] = visited[x] + 1
        q.append(x - 1)

    if 0 <= x + 1 < MAX and visited[x + 1] == -1:
        visited[x + 1] = visited[x] + 1
        q.append(x + 1)

print(visited[k])
