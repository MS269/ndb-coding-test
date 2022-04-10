n, k = map(int, input().split())
s = list(input())

ans = 0
for i in range(n):
    if s[i] != "P":
        continue

    for j in range(max(0, i - k), min(n, i + k + 1)):
        if s[j] == "H":
            s[j] = "X"
            ans += 1
            break

print(ans)
