n = int(input())
m = int(input())


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)

    if x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x


parent = [i for i in range(n + 1)]
for i in range(1, n + 1):
    line = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if line[j] == 1:
            union_parent(i, j)

schedule = list(map(int, input().split()))
result = set([find_parent(i) for i in schedule])

print("YES" if len(result) == 1 else "NO")
