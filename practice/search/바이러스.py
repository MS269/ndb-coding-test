from collections import deque


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v):
    q = deque([v])
    ret = 0

    while q:
        v = q.popleft()

        if visited[v]:
            continue

        visited[v] = True
        ret += 1

        for i in graph[v]:
            if visited[i]:
                continue

            q.append(i)

    return ret - 1


print(bfs(1))
