from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())


def bfs(w):
    q = deque([start])
    visited = set([start])

    while q:
        x = q.popleft()

        if x == end:
            return True

        for nx, nw in graph[x]:
            if nw >= w and nx not in visited:
                q.append(nx)
                visited.add(nx)

    return False


ans = 1
left, right = 1, 10 ** 9
while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
