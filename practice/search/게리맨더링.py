from collections import deque
from itertools import combinations
from sys import maxsize


n = int(input())
populations = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in line[1:]:
        graph[i].append(j - 1)


def bfs(zone):
    x = zone[0]
    q = deque([x])
    visited = set([x])

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if nx in zone and nx not in visited:
                q.append(nx)
                visited.add(nx)

    return visited


ans = maxsize
for i in range(1, n // 2 + 1):
    zones = list(combinations(range(n), i))

    for zone in zones:
        visited1 = bfs(zone)
        visited2 = bfs([i for i in range(n) if i not in zone])

        if len(visited1) + len(visited2) == n:
            population1 = sum([populations[i] for i in visited1])
            pupulation2 = sum([populations[i] for i in visited2])
            ans = min(ans, abs(population1 - pupulation2))

print(ans if ans != maxsize else -1)
