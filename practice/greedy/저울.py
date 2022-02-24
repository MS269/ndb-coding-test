from re import A


n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = 1
for i in a:
    if ans < i:
        break

    ans += i

print(ans)
