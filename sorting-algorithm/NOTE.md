# 정렬 알고리즘(Sorting Algorithm)

정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.

## 선택 정렬(Selection Sort)

처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복**한다.

시간 복잡도: O(N^2)

```python
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프

print(arr) # 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```c++
#include <bits/stdc++.h>

using namespace std;

int n = 10;
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8}

int main() {
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[min_index] > arr[j]) {
                min_index = j;
            }
        }
        swap(arr[i], arr[min_index]);
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
}
```

```java

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        for (int i = 0; i < n; i++) {
            int min_index = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[min_index] > arr[j]) {
                    min_index = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

}
```

## 삽입 정렬(Insertion Sort)

처리되지 않은 데이터를 하나씩 골라 **적절한 위치에 삽입**한다.

선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작한다.

현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.

시간 복잡도:

- 평균의 경우: O(N^2)
- 최선의 경우(이미 정렬된 경우): O(N)

```python
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if arr[j] < arr[j - 1]: # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(arr)
```

```c++
#include <bits/stdc++.h>

using namespace std;

int n = 10;
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

int main() {
    for (int i = 1; i < n; i++) {
        for (int j = i; j > 0; j--) {
            if (arr[j] < arr[j - 1]) {
                swap(arr[j], arr[j - 1]);
            } else {
                break;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
}
```

```java
import java.util.*;

public class Main {

    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        for (int i = 1; i < n; i++) {
            for (int j = i; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;
                } else {
                    break;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

}
```

## 퀵 정렬(Quick Sort)

기준 데이터를 설정하고 그 **기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법**이다.

일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나다.

병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.

가장 기본적인 퀵 정렬은 **첫번째 데이터를 기준 데이터(Pivot)로 설정**한다.

시간 복잡도:

- 평균의 경우: O(NlogN)
- 최악의 경우(이미 정렬된 경우): O(N^2)

```python - 간결한 코드
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))
```

```c++
#include <bits/stdc++.h>

using namespace std;

int n = 10;
int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

void quickSort(int* arr, int start, int end) {
    if (start >= end) return; // 원소가 1개인 경우 종료

    int pivot = start; // 피벗은 첫 번째 원소
    int left = start + 1;
    int right = end;

    while (left <= right) {
        // 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end && arr[left] <= arr[pivot]) left++;
        // 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start && arr[right] >= arr[pivot]) right--;

        // 엇갈렸다면 작은 데이터와 피벗을 교체
        if (left > right) swap(arr[pivot], arr[right]);
        // 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else swap(arr[left], arr[right]);
    }

    // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(arr, start, right - 1);
    quickSort(arr, right + 1, end);
}

int main() {
    quickSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << ' ';
    }
}
```

```java
import java.util.*;

public class Main {

    public static void quickSort(int[] arr, int start, int end) {
        if (start >= end) return;

        int pivot = start;
        int left = start + 1;
        int right = end;

        while (left <= right) {
            while (left <= end && arr[left] <= arr[pivot]) left++;
            while (right > start && arr[right] >= arr[pivot]) right--;

            if (left > right) {
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            } else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }

        quickSort(arr, start, right - 1);
        quickSort(arr, right + 1, end);
    }

    public static void main(String[] args) {
        int n = 10;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        quickSort(arr, 0, n - 1);

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }

}
```

## 계수 정렬(Counting Sort)

특정 조건이 부합할 때만 사용할 수 있지만 **매우 빠르게 동작하는** 정렬 알고리즘이다.

계수 정렬은 **데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때** 사용 가능하다.

데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N + K)를 보장한다.

계수 정렬의 시간 복잡도와 공간 복잡도는 모두 **O(N + K)**이다.

계수 정렬은 **동일한 값을 가지는 데이터가 여러 개 등장할 때** 효과적으로 사용할 수 있다.

계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다.
데이터가 0과 999,999로 단 2개만 존재하는 경우를 예로 들 수 있다.

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
cnt = [0] * (max(arr) + 1)

for i in range(len(arr)):
    cnt[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(cnt)): # 리스트에 기록된 정렬 정보 확인
    for j in range(cnt[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

```c++
#include <bits/stdc++.h>

#define MAX_VALUE 9

using namespace std;

int n = 15;
int arr[15] = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
int cnt[MAX_VALUE + 1];

int main(void) {
    for (int i = 0; i < n; i++) {
        cnt[arr[i]] += 1;
    }

    for (int i = 0; i <= MAX_VALUE; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            cout << i << ' ';
        }
    }
}
```

```java
import java.util.*;

public class Main {

    public static final int MAX_VALUE = 9;

    public static void main(String[] args) {
        int n = 15;
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
        int[] cnt = new int[MAX_VALUE + 1];

        for (int i = 0; i < n; i++) {
            cnt[arr[i]] += 1;
        }

        for (int i = 0; i <= MAX_VALUE; i++) {
            for (int j = 0; j < cnt[i]; j++) {
                System.out.print(i + " ");
            }
        }
    }

}
```

## 정렬 알고리즘 비교하기

대부분의 프로그래밍 언어에서 지원하는 **표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장**한다.

| 정렬 알고리즘 | 평균 시간 복잡도 | 공간 복잡도 | 특징                                                                           |
| :-----------: | :--------------: | :---------: | :----------------------------------------------------------------------------- |
|   선택 정렬   |      O(N^2)      |    O(N)     | 아이디어가 매우 간단하다.                                                      |
|   삽입 정렬   |      O(N^2)      |    O(N)     | 데이터가 거의 정렬되어 있을 때는 가장 빠르다.                                  |
|    퀵 정렬    |     O(NlogN)     |    O(N)     | 대부분의 경우에 가장 적합하며, 충분히 빠르다.                                  |
|   계수 정렬   |     O(N + K)     |  O(N + K)   | 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다. |
