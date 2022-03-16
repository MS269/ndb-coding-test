from collections import deque


n, k = map(int, input().split())


def bfs():
    q = deque([n])
    visited = [-1] * 100001
    visited[n] = 0
    path = [0] * 100001

    while q:
        x = q.popleft()

        if x == k:
            ans = []
            while x != n:
                ans.append(x)
                x = path[x]
            ans.append(n)
            ans.reverse()

            print(visited[k])
            print(" ".join(map(str, ans)))
            return

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 100000 and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
                path[nx] = x


bfs()
