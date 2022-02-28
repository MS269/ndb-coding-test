import sys


sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def dfs(fr, wei):
    for to, w in graph[fr]:
        if dist[to] == -1:
            dist[to] = wei + w
            dfs(to, wei + w)


dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)

fr = dist.index(max(dist))
dist = [-1] * (n + 1)
dist[fr] = 0
dfs(fr, 0)

print(max(dist))
