from sys import maxsize


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[maxsize] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:
        if graph[x][0]:
            return graph[x][0]
        return maxsize

    if dp[x][visited] != maxsize:
        return dp[x][visited]

    for i in range(1, n):
        if not graph[x][i]:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], dfs(
            i, visited | (1 << i)) + graph[x][i])

    return dp[x][visited]


print(dfs(0, 1))
