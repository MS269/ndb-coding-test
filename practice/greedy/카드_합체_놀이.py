import heapq


n, m = map(int, input().split())
a = list(map(int, input().split()))

heapq.heapify(a)

for _ in range(m):
    x = heapq.heappop(a)
    y = heapq.heappop(a)

    heapq.heappush(a, x + y)
    heapq.heappush(a, x + y)

print(sum(a))
