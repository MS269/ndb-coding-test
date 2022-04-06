n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

cnts = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 1:
            cnts[i] += 1
            cnts[j] += 1

print(cnts.count(n - 1))
