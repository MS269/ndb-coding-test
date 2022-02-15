# 파이썬(Python) 노트

## 유니코드

```py
a = ord("a") # 97
b = chr(97) # a
```

## 큐(Queue)

```py
from collections import deque

q = deque()
q.append(a)
b = q.popleft()
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
