from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

lower = bisect_left(arr, x)
upper = bisect_right(arr, x)

result = upper - lower
print(result if result != 0 else -1)
