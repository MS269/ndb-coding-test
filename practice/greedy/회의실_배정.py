n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

schedule.sort()

ans = 0
temp = 0

for time in schedule:
    start, end = time

    if start >= temp:
        ans += 1
        temp = end
    elif end <= temp:
        temp = end

print(ans)
