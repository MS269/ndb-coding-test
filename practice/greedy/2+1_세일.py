n = int(input())
c = [int(input()) for _ in range(n)]

c.sort(reverse=True)

for i in range(2, n, 3):
    c[i] = 0

print(sum(c))
