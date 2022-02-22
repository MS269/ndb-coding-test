from collections import deque


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

rx, ry = 0, 0
bx, by = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            rx, ry = i, j
        elif graph[i][j] == "B":
            bx, by = i, j


def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by)])
    visited = [(rx, ry, bx, by)]
    cnt = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if cnt > 10:
                return -1

            if graph[rx][ry] == 'O':
                return cnt

            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]

                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break

                    if graph[nrx][nry] == 'O':
                        break

                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]

                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break

                    if graph[nbx][nby] == 'O':
                        break

                if graph[nbx][nby] == 'O':
                    continue

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))

        cnt += 1

    return -1


print(bfs(rx, ry, bx, by))
