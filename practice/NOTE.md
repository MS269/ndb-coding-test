# 파이썬(Python) 노트

- 큐(Queue)

```py
from collections import deque

q = deque()
q.append(a)
b = q.popleft()
```

- RecursionError 해결법

```py
import sys

sys.setrecursionlimit(1000000)
```
