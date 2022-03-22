n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.sort(key=lambda x: [-x[1], x[0]])

scores = [0] * (max([a[i][0] for i in range(n)]) + 1)
for i in range(n):
    for j in range(a[i][0], 0, -1):
        if scores[j] == 0:
            scores[j] = a[i][1]
            break

print(sum(scores))
