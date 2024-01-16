# Sort (정렬)

# **거품 정렬(Bubble Sort)**

![](https://blog.kakaocdn.net/dn/nsZ8p/btrAIf9uNf6/oMrfjknBSpMQPEkUQgNZ71/img.gif)

배열의 0번 칸이 1번 칸 보다 크다면 두 값의 위치를 교환한다.

배열의 1번 칸이 2번 칸 보다 크다면 두 값의 위치를 교환한다.

배열의 2번 칸이 3번 칸 보다 크다면 두 값의 위치를 교환한다.

 ~

배열의 n-2번 칸이 n-1번 칸 보다 크다면 두 값의 위치를 교환한다.

### 코드 구현

```python
def bubble_sort(arr):
    n = len(arr)

    # 모든 요소에 대해 반복
    for i in range(n):
        # 마지막 i개의 요소는 이미 정렬되었으므로 제외
        for j in range(0, n-i-1):
            # 현재 요소가 다음 요소보다 크면 서로 교환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 정렬할 리스트
my_list = [64, 34, 25, 12, 22, 11, 90]

# 거품 정렬 수행
bubble_sort(my_list)

# 정렬된 결과 출력
print("정렬된 리스트:", my_list)
```

### **선택 정렬(Selection Sort)**

![https://blog.kakaocdn.net/dn/cqCvsg/btrAVs0WT4A/zuxAMlsX5t758nSa6MwvK1/img.gif](https://blog.kakaocdn.net/dn/cqCvsg/btrAVs0WT4A/zuxAMlsX5t758nSa6MwvK1/img.gif)

0 배열 내에서 가장 작은 값

1 첫 번째 값을 제외하고 남은 배열 값 중에서 가장 작은 값

~

n-1 마지막에 남은 값

### 코드 구현

```python
def selection_sort(arr):
    n = len(arr)

    # 리스트를 돌면서 가장 작은 값을 찾아 앞으로 이동
    for i in range(n):
        # 현재 인덱스를 최소값으로 설정
        min_index = i

        # 현재 인덱스 다음부터 끝까지 순회하며 최소값을 찾음
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # 현재 인덱스와 최소값을 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 정렬할 리스트
my_list = [64, 25, 12, 22, 11]

# 선택 정렬 수행
selection_sort(my_list)

# 정렬된 결과 출력
print("정렬된 리스트:", my_list)
```

# **삽입 정렬(Insertion Sort)**

![https://blog.kakaocdn.net/dn/rGBXh/btrASwpIeko/TLrkTXTvJwRQvp7QOzhC2K/img.gif](https://blog.kakaocdn.net/dn/rGBXh/btrASwpIeko/TLrkTXTvJwRQvp7QOzhC2K/img.gif)

자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교 하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘

### 코드 구현

```python
def insertion_sort(arr):
    n = len(arr)

    # 리스트를 돌면서 각 요소를 적절한 위치에 삽입
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # key보다 큰 원소들을 오른쪽으로 이동
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # key를 적절한 위치에 삽입
        arr[j + 1] = key

# 정렬할 리스트
my_list = [12, 11, 13, 5, 6]

# 삽입 정렬 수행
insertion_sort(my_list)

# 정렬된 결과 출력
print("정렬된 리스트:", my_list)
```

# **퀵 정렬(Quick Sort)**

![https://blog.kakaocdn.net/dn/dIqOwt/btrAVtyN6CV/LFxg1TL5OrdcWAuwMInIzk/img.gif](https://blog.kakaocdn.net/dn/dIqOwt/btrAVtyN6CV/LFxg1TL5OrdcWAuwMInIzk/img.gif)

하나의 리스트를 피벗(pivot)을 기준으로 두 개의 비균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.

[https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html](https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html)

### 코드 구현

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# 정렬할 리스트
my_list = [12, 4, 5, 6, 7, 3, 1, 15]

# 퀵 정렬 수행
sorted_list = quick_sort(my_list)

# 정렬된 결과 출력
print("정렬된 리스트:", sorted_list)
```

# 합병 **정렬(Merge Sort)**

![https://blog.kakaocdn.net/dn/bpXxX7/btrBzUvXZOf/RCAxQSEte1x8DmwbZaRLO0/img.gif](https://blog.kakaocdn.net/dn/bpXxX7/btrBzUvXZOf/RCAxQSEte1x8DmwbZaRLO0/img.gif)

하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음, 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.
[https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html](https://gmlwjd9405.github.io/2018/05/08/algorithm-merge-sort.html)

### 코드 구현

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 리스트를 반으로 나눔
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 각 반을 재귀적으로 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 정렬된 두 반을 병합
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # 두 반 중 하나라도 남아있을 때까지 반복
    while i < len(left) and j < len(right):
        # 작은 값을 결과에 추가
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남아있는 요소들을 결과에 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 정렬할 리스트
my_list = [12, 11, 13, 5, 6, 7]

# 병합 정렬 수행
sorted_list = merge_sort(my_list)

# 정렬된 결과 출력
print("정렬된 리스트:", sorted_list)
```

# **힙 정렬(Heap Sort)**

![https://blog.kakaocdn.net/dn/b99Tq3/btrBzdWOH3Q/eUl45KKk06dKtYO19HWnbk/img.gif](https://blog.kakaocdn.net/dn/b99Tq3/btrBzdWOH3Q/eUl45KKk06dKtYO19HWnbk/img.gif)

힙(Heap)이란 이진트리의 형태로 만들어진 자료구조

1. 값을 트리에 넣음
2. 만약 부모노드가 자식노드보다 작다면 swap 후 트리에 넣음
3. 부모노드가 자식노드보다 크면 그대로 진행
4. (2)로 돌아가 반복
- 자식노드끼리는 비교하지 않는다.
    
    → 최대 or 최소를 구할 때 사용
    

### 코드 구현

```python
def heap_sort(arr):
    n = len(arr)

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 하나씩 요소 추출하며 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최대값(루트)을 배열 끝과 교환
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # 왼쪽 자식이 루트보다 크면 largest를 왼쪽 자식으로 설정
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # 오른쪽 자식이 루트보다 크면 largest를 오른쪽 자식으로 설정
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # largest가 변경되었으면 루트와 largest 위치의 요소 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 변경된 위치에서 다시 heapify 호출
        heapify(arr, n, largest)

# 정렬할 리스트
my_list = [12, 11, 13, 5, 6, 7]

# 힙 정렬 수행
heap_sort(my_list)

# 정렬된 결과 출력
print("정렬된 리스트:", my_list)
```

# 파이썬 내장함수 `.sort()`

- **Timsort(팀소트)** 를 사용한다.
    - 삽입정렬 + 병합정렬
- 팀소트는 파이썬의 리스트와 튜플과 같은 시퀀스 타입을 정렬하는 데에 사용되며, 안정적인 정렬을 보장한다.  안정적인 정렬은 동일한 키를 가진 요소들의 상대적인 순서가 정렬 전과 동일하게 유지되는 것을 의미한다.
