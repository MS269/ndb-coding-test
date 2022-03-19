from collections import deque


def bfs():
    q = deque([(start[0], start[1])])
    visited = [False] * n

    while q:
        x, y = q.popleft()

        if abs(end[0] - x) + abs(end[1] - y) <= 1000:
            return True

        for i in range(n):
            if abs(stores[i][0] - x) + abs(stores[i][1] - y) <= 1000 and not visited[i]:
                q.append((stores[i][0], stores[i][1]))
                visited[i] = True

    return False


for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))

    print("happy" if bfs() else "sad")
