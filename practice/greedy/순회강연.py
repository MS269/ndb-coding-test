import heapq


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: x[1])

pq = []
for p, d in a:
    heapq.heappush(pq, p)

    if len(pq) > d:
        heapq.heappop(pq)

print(sum(pq))
