from collections import deque


f, s, g, u, d = map(int, input().split())

q = deque([s])
visited = [0] * (f + 1)
visited[s] = 1
while q:
    x = q.popleft()

    if x == g:
        break

    for dx in [u, -d]:
        nx = x + dx

        if 1 <= nx <= f and not visited[nx]:
            q.append(nx)
            visited[nx] = visited[x] + 1

print(visited[g] - 1 if visited[g] != 0 else "use the stairs")
