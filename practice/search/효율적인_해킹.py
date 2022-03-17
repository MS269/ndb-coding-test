from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(x):
    q = deque([x])
    visited = [False] * (n + 1)
    visited[x] = True
    cnt = 1

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = True
                cnt += 1

    return cnt


max_cnt = 0
ans = []
for i in range(1, n + 1):
    cnt = bfs(i)

    if cnt > max_cnt:
        max_cnt = cnt
        ans = [i]
    elif cnt == max_cnt:
        ans.append(i)

print(*ans)
