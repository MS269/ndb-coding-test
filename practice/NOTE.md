# 파이썬(Python) 노트

## 유니코드

```py
a = ord("a") # 97
b = chr(97) # a
```

## 큐(Queue)

```py
from collections import deque

q = deque([1, 2, 3, 4, 5])
q.append(0)
a = q.popleft() # 1
```

## 우선순위 큐(Priority Queue)

```py
import heapq # min heap

pq = [1, 2, 3, 4, 5]
heapq.heapify(pq)
heapq.heappush(pq, 0)
b = heapq.heappop(pq) # 0
```

## RecursionError 해결법

```py
import sys

sys.setrecursionlimit(10 ** 6)
```

## 깊은 복사(Deep Copy)

```py
import copy

a = [1, 2, 3, 4, 5]
b = copy.deepcopy(a)
```
