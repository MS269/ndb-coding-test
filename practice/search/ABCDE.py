import sys


sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, c):
    global ans

    if c == 5:
        ans = 1
        return

    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx, c + 1)
            visited[nx] = False


ans = 0
for i in range(n):
    if ans == 1:
        break

    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(ans)
