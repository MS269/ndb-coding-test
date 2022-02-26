a = input()
b = input()

ans = 0
i = 0
while i <= len(a) - len(b):
    if a[i:i + len(b)] == b:
        ans += 1
        i += len(b)
    else:
        i += 1

print(ans)
