n = int(input())
graph = list(map(int, input().split()))
m = int(input())


def dfs(v):
    graph[v] = -2

    for i in range(n):
        if graph[i] == v:
            dfs(i)


dfs(m)

ans = 0
for i in range(n):
    if i not in graph and graph[i] != -2:
        ans += 1

print(ans)
