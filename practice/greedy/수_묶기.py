n = int(input())
a = [int(input()) for _ in range(n)]

positive = [i for i in a if i > 0]
negative = [i for i in a if i <= 0]

positive.sort()
negative.sort(reverse=True)

ans = 0

while positive:
    a = positive.pop()

    if positive:
        b = positive.pop()
        ans += max(a + b, a * b)
    else:
        ans += a

while negative:
    a = negative.pop()

    if negative:
        b = negative.pop()
        ans += a * b
    else:
        ans += a

print(ans)
