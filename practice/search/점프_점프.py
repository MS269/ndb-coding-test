from collections import deque


n = int(input())
a = list(map(int, input().split()))


def bfs():
    q = deque([0])
    visited = [-1] * n
    visited[0] = 0

    while q:
        x = q.popleft()

        for nx in range(x + 1, x + a[x] + 1):
            if 0 <= nx < n and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1

    return visited[n - 1]


print(bfs())
