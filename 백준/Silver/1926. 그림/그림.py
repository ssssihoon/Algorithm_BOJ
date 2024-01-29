'''

bfs를 모두 순회하는 것은 이중 for 문으로 모든 수를 다 돌아야한다. 초기화는 필요없음 왜냐면
모든 지점에서의 경우의 수를 보는 것이 아니라 다음으로 넘어가려고 하는 것이기 때문
여기서 max넓이를 구함. 그리고 개수 구하는 것은 어떻게? ?? -> 검색 ㄱㄱ

'''



from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

paint = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))

if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))

