from collections import deque


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q = deque([(x, 0)])
    visited = [False] * (n + 1)
    visited[x] = True
    cnt = 0

    while q:
        x, c = q.popleft()

        if c <= 2:
            cnt += 1

        for nx in graph[x]:
            if not visited[nx]:
                q.append((nx, c + 1))
                visited[nx] = True

    return cnt - 1


print(bfs(1))
