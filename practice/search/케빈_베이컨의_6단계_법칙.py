from collections import deque


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    dist = [0] * (n + 1)

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                dist[i] = dist[v] + 1

    return sum(dist)


bacon = []
for i in range(1, n + 1):
    bacon.append(bfs(i))

print(bacon.index(min(bacon)) + 1)
