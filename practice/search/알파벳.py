def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if not alphabets[graph[nx][ny]]:
            alphabets[graph[nx][ny]] = True
            dfs(nx, ny, cnt + 1)
            alphabets[graph[nx][ny]] = False


r, c = map(int, input().split())
graph = [list(map(lambda x: ord(x) - 65, input())) for _ in range(r)]
alphabets = [False] * 26
ans = 0

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

alphabets[graph[0][0]] = True
dfs(0, 0, 1)

print(ans)
