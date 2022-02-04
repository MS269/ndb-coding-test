n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

s = []
for i in range(n):
    s.append(a[i] * b[i])

print(sum(s))
