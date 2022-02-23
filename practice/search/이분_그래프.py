import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(v, s):
    visited[v] = s

    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -s):
                return False
        elif visited[i] == visited[v]:
            return False

    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_yes = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            if not dfs(i, 1):
                is_yes = False
                break

    print('YES' if is_yes else 'NO')
