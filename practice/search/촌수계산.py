n = int(input())
v1, v2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = -1


def dfs(v, c):
    if v == v2:
        global ans
        ans = c

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, c + 1)


dfs(v1, 0)

print(ans)
