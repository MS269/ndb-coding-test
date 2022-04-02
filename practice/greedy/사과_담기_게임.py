n, m = map(int, input().split())
j = int(input())
a = [int(input()) for _ in range(j)]

ans = 0
pos = 1
for basket in a:
    if basket < pos:
        ans += pos - basket
        pos = basket
    elif basket > pos + m - 1:
        ans += basket - (pos + m - 1)
        pos = basket - (m - 1)

print(ans)
