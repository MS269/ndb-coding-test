n = int(input())
t = list(map(int, input().split()))

t.sort(reverse=True)

print(max([t[i] + i for i in range(n)]) + 2)
