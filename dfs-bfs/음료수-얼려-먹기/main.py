n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
        if dfs(i, j) == True:
            result += 1

print(result)
