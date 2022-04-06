from collections import deque


n = int(input())
times = [0] * (n + 1)
builds = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    line = list(map(int, input().split()))
    times[i] = line[0]
    for j in line[1:-1]:
        builds[j].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

ans = [0] * (n + 1)
while q:
    x = q.popleft()
    ans[x] += times[x]

    for nx in builds[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

        ans[nx] = max(ans[nx], ans[x])

print(*ans[1:], sep="\n")
