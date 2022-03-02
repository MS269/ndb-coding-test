from collections import deque


for _ in range(int(input())):
    a, b = map(int, input().split())

    q = deque([(a, "")])
    visited = [False] * 10000
    while q:
        n, s = q.popleft()

        if n == b:
            print(s)
            break

        temp = (2 * n) % 10000
        if not visited[temp]:
            q.append((temp, s + "D"))
            visited[temp] = True

        temp = (n - 1) % 10000
        if not visited[temp]:
            q.append((temp, s + "S"))
            visited[temp] = True

        temp = (n * 10 + n // 1000) % 10000
        if not visited[temp]:
            q.append((temp, s + "L"))
            visited[temp] = True

        temp = ((n % 10) * 1000 + n // 10) % 10000
        if not visited[temp]:
            q.append((temp, s + "R"))
            visited[temp] = True
