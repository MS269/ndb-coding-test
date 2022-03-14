s = input()

abbr = "UCPC"
idx = 0
for i in s:
    if idx == 4:
        break

    if i == abbr[idx]:
        idx += 1

print("I love UCPC" if idx == 4 else "I hate UCPC")
