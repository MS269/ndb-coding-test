# 그래프 탐색 알고리즘: DFS/BFS

탐색(Search)이란 많은 양의 데이터 중에서 **원하는 데이터를 찾는 과정**을 말한다.

## 스택(Stack) 자료구조

**먼저 들어온 데이터가 나중에 나가는 형식(선입후출)**의 자료구조다.

**입구와 출구가 동일한 형태로** 스택을 시각화할 수 있다.

삽입과 삭제 두 연산으로 구성된다.

```python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력, 먼저 나갈 원소부터 출력 / 출력:[1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력, 먼저 들어온 원소부터 출력 / 출력:[5, 2, 3, 1]
```

```c++
#include <bits/stdc++.h>

using namespace std;

stack<int> s;

int main(void) {
    s.push(5);
    s.push(2);
    s.push(3);
    s.push(7);
    s.pop();
    s.push(1);
    s.push(4);
    s.pop();

    // 스택의 최상단 원소부터 출력 / 출력:1 3 2 5
    while (!s.empty()) {
        cout << s.top() << ' ';
        s.pop();
    }

    return 0;
}
```

```java
import java.util.Stack

public class Main {

    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();

        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();

        // 스택의 최상단 원소부터 출력 / 출력:1 3 2 5
        while (!s.empty()) {
            System.out.print(s.peek() + " ");
            s.pop();
        }
    }

}
```

## 큐(Queue) 자료구조

**먼저 들어온 데이터가 먼저 나가는 형식(선입선출)**의 자료구조다.

**입구와 출구가 모두 뚫려 있는 터널과 같은 형태**로 시각화 할 수 있다.

삽입과 삭제 두 연산으로 구성된다.

```python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용(리스트로도 가능하지만 시간복잡도의 차이가 있음)
q = deque()

q.append(5)
q.append(2)
q.append(3)
q.append(7)
q.popleft()
q.append(1)
q.append(4)
q.popleft()

print(q) # 먼저 들어온 순서대로 출력 / 출력:deque([3, 7, 1, 4])
q.reverse() # 역순으로 바꾸기
print(q) # 나중에 들어온 순서대로 출력 / 출력:deque([4, 1, 7, 3])
```

```c++
#include <bits/stdc++.h>

using namespace std;

queue<int> q;

int main(void) {
    q.push(5);
    q.push(2);
    q.push(3);
    q.push(7);
    q.pop();
    q.push(1);
    q.push(4);
    q.pop();

    // 먼저 들어온 원소부터 추출 / 출력:3 7 1 4
    while (!q.empty()) {
        cout << q.front() << ' ';
        q.pop();
    }

    return 0;
}
```

```java
import java.util.LinkedList
import java.util.Queue

public class Main {

    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();

        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();
        q.offer(1);
        q.offer(4);
        q.poll();

        // 먼저 들어온 원소부터 추출 / 출력:3 7 1 4
        while (!q.empty()) {
            System.out.print(q.pool() + " ");
        }
    }

}
```

## 재귀 함수(Recursive Function)

**자기 자신을 다시 호출하는 함수**를 의미한다.

재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.

모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.

컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

### 팩토리얼 구현 예제

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1

    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i

    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1

    # n! = n * (n - 1)!를 그대로 코드로 작성
    return n * factorial_recursive(n - 1)
```

재귀적으로 구현한 것은 수학적으로 정의된 점화식을 그대로 이용하여 더 간결하고 직관적이다.

### 최대공약수(Greatest Common Divisor) 계산 예제

두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로는 유클리드 호제법이 있다.

#### 유클리드 호제법(Euclidean Algorithm)

- 두 자연수 A, B,에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 합시다.
- 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.
- ex) GCD(192, 162) = GCD(162, 30) = GCD(30, 12) = GCD(12, 6) = 6

```python
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
```

## DFS(Depth-First Search)

**깊이 우선 탐색**이라고도 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**이다.

**스택 자료구조(혹은 재귀 함수)를 이용**하며, 구체적인 동작 과정은 다음과 같다.

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최산단 노드를 꺼낸다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

```python
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출 / 출력:1 2 7 6 8 3 4 5
dfs(graph, 1, visited)
```

```c++
#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> graph[9];

void dfs(int x) {
    visited[x] = true;
    cout << x << ' ';

    for (int i = 0; i < graph[x].size(); i++) {
        int y = graph[x][i];
        if (!visited[y]) {
            dfs(y);
        }
    }
}

int main(void) {
    // 노드 1에 연결된 노드 정보 저장
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);

    // 노드 정보 저장 생략

    // 노드 8에 연결된 노드 정보 저장
    graph[8].push_back(1);
    graph[8].push_back(7);

    dfs(1);

    return 0;
}
```

```java
import java.util.ArrayList;

public class Main {

    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void dfs(int x) {
        visited[x] = true;
        System.out.print(x + " ");

        for (int i = 0; i < graph.get(x).size(); i++) {
            int y = graph.get(x).get(i);
            if (!visited[y]) {
                dfs(y);
            }
        }
    }

    public static void main(String[] args) {
        // 그래프 초기화
        for (int i = 0; i < 9; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 노드 1에 연결된 노드 정보 저장
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);

        // 노드 정보 저장 생략

        // 노드 8에 연결된 노드 정보 저장
        graph.get(8).add(1);
        graph.get(8).add(7);

        dfs(1);
    }

}
```

## BFS(Breadth-First Search)

**너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**이다.

**큐 자료구조를 이용**하며, 구체적인 동작 과정은 다음과 같다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    q = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 출력
        v = q.popleft()
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출 / 출력: 1 2 3 8 7 4 5 6
bfs(graph, 1, visited)
```

```c++
#include <bits/stdc++.h>

using namespace std;

bool visited[9];
vector<int> graph[9];

void bfs(int start) {
    queue<int> q;
    q.push(start);

    visited[start] = true;

    while(!q.empty()) {
        int x = q.front();
        q.pop();
        cout << x << ' ';

        for(int i = 0; i < graph[x].size(); i++) {
            int y = graph[x][i];
            if(!visited[y]) {
                q.push(y);
                visited[y] = true;
            }
        }
    }
}

int main(void) {
    // 노드 1에 연결된 노드 정보 저장
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);

    // 노드 정보 저장 생략

    // 노드 8에 연결된 노드 정보 저장
    graph[8].push_back(1);
    graph[8].push_back(7);

    bfs(1);

    return 0;
}
```

```java
import java.util.*;

public class Main {

    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);

        visited[start] = true;

        while(!q.isEmpty()) {
            int x = q.poll();
            System.out.print(x + " ");

            for(int i = 0; i < graph.get(x).size(); i++) {
                int y = graph.get(x).get(i);
                if(!visited[y]) {
                    q.offer(y);
                    visited[y] = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        // 그래프 초기화
        for (int i = 0; i < 9; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // 노드 1에 연결된 노드 정보 저장
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);

        // 노드 정보 저장 생략

        // 노드 8에 연결된 노드 정보 저장
        graph.get(8).add(1);
        graph.get(8).add(7);

        bfs(1);
    }

}
```
