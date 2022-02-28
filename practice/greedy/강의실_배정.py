import heapq


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort()

pq = [a[0][1]]
for i in range(1, n):
    if a[i][0] < pq[0]:
        heapq.heappush(pq, a[i][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, a[i][1])

print(len(pq))
