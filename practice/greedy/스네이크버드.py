n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for i in a:
    if i > l:
        break

    l += 1

print(l)
