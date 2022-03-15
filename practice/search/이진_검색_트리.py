import sys


sys.setrecursionlimit(10 ** 6)

graph = []
while True:
    try:
        graph.append(int(input()))
    except:
        break


def dfs(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        if graph[i] > graph[start]:
            mid = i
            break

    dfs(start + 1, mid - 1)
    dfs(mid, end)
    print(graph[start])


dfs(0, len(graph) - 1)
