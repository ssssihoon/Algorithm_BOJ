N, K = map(int, input().split())
h = list(map(int, input().split()))
difference = []
sum = 0
for i in range(0, N-1):
    difference.append(h[i+1]-h[i])

difference.sort()
for i in range(0, N-K):
    sum += difference[i]
print(sum)


'''
N명의 원생들을 키순서로 일렬로 줄을 세움
K의 개의 조로 나눔 (적어도 한명 이상) -> 순열? nPr
같은 조에 속한 원생들은 인접
조별로 인원수가 같을 필요 없음

티셔츠 비용 -> 조에서 가장 키큰 원생 - 작은 원생
K개의 조에 대해 티셔츠의 비용 합을 최소로 하고 싶다.


1 3 5 6 10
 2 2 1 4


 
5 3
1 3 5 6 10
'''
