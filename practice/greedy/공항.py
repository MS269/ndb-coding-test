g = int(input())
p = int(input())
a = [int(input()) for _ in range(p)]

parent = {i: i for i in range(g + 1)}


def find_parent(a):
    if parent[a] == a:
        return a

    parent[a] = find_parent(parent[a])

    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    parent[b] = a


ans = 0
for i in a:
    x = find_parent(i)

    if x == 0:
        break

    ans += 1
    union(x - 1, x)

print(ans)
