from collections import deque


v = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(v):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp) - 2, 2):
        graph[temp[0]].append((temp[i], temp[i + 1]))


def bfs(start):
    q = deque([start])
    visited = [-1] * (v + 1)
    visited[start] = 0

    while q:
        start = q.popleft()

        for end, edge in graph[start]:
            if visited[end] == -1:
                q.append(end)
                visited[end] = visited[start] + edge

    return visited


distances1 = bfs(1)
distances2 = bfs(distances1.index(max(distances1)))

print(max(distances2))
