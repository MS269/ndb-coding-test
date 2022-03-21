from collections import deque


prime_numbers = [True] * 10000
prime_numbers[0] = False
prime_numbers[1] = False
for i in range(2, 10000):
    if prime_numbers[i]:
        for j in range(i + i, 10000, i):
            prime_numbers[j] = False

for _ in range(int(input())):
    a, b = map(int, input().split())

    q = deque([(a, 0)])
    visited = [False] * 10000
    visited[a] = True
    ans = -1

    while q:
        x, c = q.popleft()

        if x == b:
            ans = c
            break

        sx = str(x)

        for i in range(4):
            for j in range(10):
                nx = int(sx[:i] + str(j) + sx[i + 1:])

                if 1000 <= nx < 10000 and prime_numbers[nx] and not visited[nx]:
                    q.append((nx, c + 1))
                    visited[nx] = True

    print(ans if ans != -1 else "Impossible")
