from collections import deque


n, k = map(int, input().split())


def bfs(n, k):
    q = deque([(n, 0)])
    visited = [False] * 100001
    visited[n] = 0

    while q:
        x, s = q.popleft()

        if x == k:
            return s

        for nx in [2 * x, x + 1, x - 1]:
            if nx < 0 or nx > 100000:
                continue
            if visited[nx]:
                continue

            q.append((nx, s + 1))
            visited[nx] = True

    return -1


print(bfs(n, k))
