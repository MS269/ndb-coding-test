# 소수(Prime Number)

소수란 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수이다.

## 소수의 판별: 기본적인 알고리즘

```python
# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
        return True # 소수임
```

```java
// 소수 판별 함수(2이상의 자연수에 대하여)
public static boolean isPrimeNumber(int x) {
    // 2부터 (x - 1)까지의 모든 수를 확인하며
    for (int i = 2; i < x; i++) {
        // x가 해당 수로 나누어떨어진다면
        if (x % i == 0) {
            return false; // 소수가 아님
        }
        return true; // 소수임
    }
}
```

### 소수의 판별: 기본적인 알고리즘 성능 분석

2부터 x - 1까지의 모든 자연수에 대하여 연산을 수행해야 한다.

- 모든 수를 하나씩 확인한다는 점에서 시간 복잡도는 O(X)이다.

## 약수(divisor)의 성질

**모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭**을 이룬다.

따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 **가운데 약수(제곱근)까지만 확인**하면 된다.

### 소수의 판별: 개선된 알고리즘

```python
# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(x ** 0.5)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
```

```java
public static boolean isPrimeNumber(int x) {
    // 2부터 x의 제곱근까지의 모든 수를 확인하며
    for (int i = 2; i <= Math.sqrt(x); i++) {
        // x가 해당 수로 나누어떨어진다면
        if (x % i == 0) {
            return false; // 소수가 아님
        }
    }
    return true; // 소수임
```

## 다수의 소수 판별

특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할 때는 어떻게 할까?

- **에라토스테네스의 체 알고리즘**을 사용한다.

### 에라토스테네스의 체 알고리즘(Sieve of Eratosthenes)

**다수의 자연수에 대하여 소수 여부를 판별**할 때 사용하는 대표적인 알고리즘이다.

N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

**구체적인 동작 과정**은 다음과 같다.

1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다(i는 제거하지 않는다).
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

```python
import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
```

```java
import java.util.*;

class Main {

    public static int n = 1000; // 2부터 1,000까지의 모든 수에 대하여 소수 판별
    public static boolean[] arr = new boolean[n + 1];

    public static void main(String[] args) {
        Arrays.fill(arr, true); // 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

        // 에라토스테네스의 체 알고리즘 수행
        // 2부터 n의 제곱근까지의 모든 수를 확인하며
        for (int i = 2; i <= Math.sqrt(n); i++) {
            // i가 소수인 경우(남은 수인 경우)
            if (arr[i] == true) {
                // i를 제외한 i의 모든 배수를 지우기
                int j = 2;
                while (i * j <= n) {
                    arr[i * j] = false;
                    j += 1;
                }
            }
        }

        // 모든 소수 출력
        for (int i = 2; i <= n; i++) {
            if (arr[i]) System.out.print(i + " ");
        }
    }

}
```

#### 에라토스테네스의 체 알고리즘 성능분석

에라토스테네스의 체 알고리즘의 시간 복잡도는 O(NloglogN)이다.

에라토스테네스의 체 알고리즘은 다수의 소수를 찾아햐 하는 문제에서 효과적으로 사용될 수 있다.

- 하지만 각 자연수에 대한 소수 여부를 저장해야 하므로 **메모리가 많이 필요**하다.
- **10억**이 소수인지 아닌지 판별해야 할 때 에라토스테네스의 체를 사용할 수 있을까요?
