import heapq

n = int(input())
pq = [int(input()) for _ in range(n)]

heapq.heapify(pq)

ans = 0
while len(pq) > 1:
    card = heapq.heappop(pq) + heapq.heappop(pq)
    ans += card
    heapq.heappush(pq, card)

print(ans)
