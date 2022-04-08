from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(x):
    q = deque([x])
    visited[x] = 0

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1


bfs(x)

ans = []
for i in range(1, n + 1):
    if visited[i] == k:
        ans.append(i)

if ans:
    print(*ans, sep="\n")
else:
    print(-1)
