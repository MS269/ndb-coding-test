from collections import deque


a, b = map(int, input().split())


def bfs():
    q = deque([(a, 1)])

    while q:
        x, c = q.popleft()

        if x == b:
            return c

        nx = 2 * x
        if a <= nx <= b:
            q.append((nx, c + 1))

        nx = x * 10 + 1
        if a <= nx <= b:
            q.append((nx, c + 1))

    return -1


print(bfs())
