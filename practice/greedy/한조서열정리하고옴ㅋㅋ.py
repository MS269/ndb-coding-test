n = int(input())
heights = list(map(int, input().split()))

ans = 0
cnt = 0
max_height = 0
for height in heights:
    if height > max_height:
        max_height = height
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)
