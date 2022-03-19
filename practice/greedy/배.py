import sys


input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    print(-1)
    sys.exit()

ans = 0
while boxes:
    ans += 1

    for crane in cranes:
        for j in range(len(boxes)):
            if crane >= boxes[j]:
                del boxes[j]
                break

print(ans)
