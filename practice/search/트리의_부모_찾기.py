import sys


sys.setrecursionlimit(10 ** 6)

n = int(input())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = [0] * (n + 1)


def dfs(fr):
    for to in tree[fr]:
        if ans[to] == 0:
            ans[to] = fr
            dfs(to)


dfs(1)

for i in range(2, n + 1):
    print(ans[i])
