t = int(input())


def solve(t):
    if t % 10 != 0:
        return -1

    a = t // 300
    t %= 300

    b = t // 60
    t %= 60

    c = t // 10
    t %= 10

    return f"{a} {b} {c}"


print(solve(t))
