t = 0
while True:
    t += 1

    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break

    print(f"Case {t}: {v // p * l + min(v % p, l)}")
