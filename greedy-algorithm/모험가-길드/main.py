n = int(input())
data = list(map(int, input().split()))

# 공포도 오름차순으로 정렬
data.sort()

result = 0
cnt = 0

for i in data:
    cnt += 1

    # 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 결성
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
