a = input().split("-")

ans = 0

for i in a[0].split("+"):
    ans += int(i)

for i in a[1:]:
    for j in i.split("+"):
        ans -= int(j)

print(ans)
